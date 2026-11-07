import unittest
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from trading_lab import Book, Order, auction_candidates, ReservationWallet, settlement_date, reconcile

class TrainingTests(unittest.TestCase):
    def test_price_time_and_partial(self):
        b=Book()
        for o in [Order('S1','SELL',25000,100),Order('S2','SELL',25000,200),Order('S3','SELL',25100,300)]: b.submit(o)
        f=b.submit(Order('B','BUY',25100,450))
        self.assertEqual([(x['maker'],x['qty']) for x in f],[('S1',100),('S2',200),('S3',150)])
        self.assertEqual(sum(x['qty']*x['price'] for x in f),11265000)
        self.assertEqual(b.orders[0].qty,150)
    def test_better_price_before_time(self):
        b=Book();b.submit(Order('old','SELL',101,10));b.submit(Order('new','SELL',100,10))
        self.assertEqual(b.submit(Order('buy','BUY',101,10))[0]['maker'],'new')
    def test_sell_crosses_best_bid(self):
        b=Book();b.submit(Order('b1','BUY',100,10));b.submit(Order('b2','BUY',101,10))
        self.assertEqual(b.submit(Order('s','SELL',99,15)),[
            {'maker':'b2','taker':'s','qty':10,'price':101},
            {'maker':'b1','taker':'s','qty':5,'price':100}])
    def test_limit_does_not_cross(self):
        b=Book();b.submit(Order('s','SELL',101,10))
        self.assertEqual(b.submit(Order('b','BUY',100,10)),[])
        self.assertEqual(len(b.orders),2)
    def test_duplicate_id_rejected_even_after_fill(self):
        b=Book();b.submit(Order('s','SELL',100,10));b.submit(Order('b','BUY',100,10))
        with self.assertRaises(ValueError): b.submit(Order('s','SELL',100,10))
    def test_invalid_order(self):
        for o in [Order('x','X',1,1),Order('x','BUY',0,1),Order('x','BUY',1,-1),Order('x','BUY',1.1,1)]:
            with self.assertRaises(ValueError): Book().submit(o)
    def test_auction_unique_volume_peak(self):
        r=auction_candidates([(100,200),(101,300),(102,100)],[(100,100),(101,300),(102,200)])
        self.assertEqual(r['candidates'],[101]);self.assertEqual(r['max_volume'],400)
    def test_auction_tie_not_silently_resolved(self):
        r=auction_candidates([(102,100)],[(100,100)])
        self.assertTrue(r['needs_tiebreak']);self.assertEqual(r['candidates'],[100,102])
    def test_auction_no_cross(self):
        self.assertEqual(auction_candidates([(99,1)],[(100,1)])['candidates'],[])
    def test_auction_empty(self):
        self.assertEqual(auction_candidates([],[])['max_volume'],0)
    def test_concurrent_reservations_do_not_overspend(self):
        w=ReservationWallet(10000000)
        with ThreadPoolExecutor(max_workers=2) as pool:
            results=list(pool.map(lambda key:w.reserve(key,6000000),['a','b']))
        self.assertEqual(sum(results),1);self.assertEqual(w.available,4000000)
    def test_duplicate_reservation_one_hold(self):
        w=ReservationWallet(100)
        self.assertTrue(w.reserve('a',60));self.assertTrue(w.reserve('a',60));self.assertEqual(w.available,40)
    def test_changed_payload_conflicts(self):
        w=ReservationWallet(100);w.reserve('a',60)
        with self.assertRaises(ValueError):w.reserve('a',61)
    def test_release_is_idempotent(self):
        w=ReservationWallet(100);w.reserve('a',60)
        self.assertEqual(w.release_confirmed('a'),60);self.assertEqual(w.release_confirmed('a'),0)
        self.assertEqual(w.available,100)
        self.assertTrue(w.reserve('a',60));self.assertEqual(w.available,100)  # Retry old intent does not recreate hold.
    def test_rejected_intent_does_not_change_on_retry(self):
        w=ReservationWallet(100);w.reserve('a',100);self.assertFalse(w.reserve('b',10))
        w.release_confirmed('a');self.assertFalse(w.reserve('b',10))
    def test_weekend_calendar(self):
        self.assertEqual(settlement_date(date(2026,11,6),2),date(2026,11,10))
    def test_holiday_calendar(self):
        self.assertEqual(settlement_date(date(2026,11,6),2,{date(2026,11,9)}),date(2026,11,11))
    def test_invalid_calendar(self):
        with self.assertRaises(ValueError):settlement_date(date(2026,11,7),2)
        with self.assertRaises(ValueError):settlement_date(date(2026,11,6),-1)
    def test_recon_missing_duplicate_and_extra(self):
        a={'id':'a','qty':1,'price':100};b={'id':'b','qty':1,'price':100};c={'id':'c','qty':1,'price':100}
        r=reconcile([a,b],[a,a,c]);self.assertEqual(r['missing'],['b']);self.assertEqual(r['extra'],['c']);self.assertEqual(r['duplicate_actual'],['a'])
    def test_equal_total_does_not_hide_wrong_ids(self):
        r=reconcile([{'id':'a','qty':1,'price':100}],[{'id':'b','qty':1,'price':100}])
        self.assertEqual(r['missing'],['a']);self.assertEqual(r['extra'],['b'])
    def test_conflicting_duplicate_and_mismatch(self):
        a={'id':'a','qty':1,'price':100};b={'id':'a','qty':2,'price':100}
        r=reconcile([a],[b,a]);self.assertEqual(r['mismatched'],['a']);self.assertEqual(r['conflict_actual'],['a'])
    def test_expected_duplicates_are_reported(self):
        a={'id':'a','qty':1,'price':100}
        self.assertEqual(reconcile([a,a],[a])['duplicate_expected'],['a'])

if __name__=='__main__':unittest.main()
