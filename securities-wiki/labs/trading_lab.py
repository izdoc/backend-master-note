"""Offline training only. Integer prices; simplified LO book, not an exchange engine."""
from dataclasses import dataclass
from datetime import date, timedelta
from collections import Counter
from threading import Lock
import json

@dataclass
class Order:
    id: str
    side: str
    price: int
    qty: int

class Book:
    """Single-threaded LO simulator. Arrival order is the time priority."""
    def __init__(self):
        self.orders = []
        self.ids = set()

    def submit(self, order):
        if (order.side not in ('BUY', 'SELL') or not order.id or
            type(order.price) is not int or type(order.qty) is not int or
            order.price <= 0 or order.qty <= 0 or order.id in self.ids):
            raise ValueError('Invalid or duplicate order')
        self.ids.add(order.id)
        incoming = Order(order.id, order.side, order.price, order.qty)
        opposite = [o for o in self.orders if o.side != incoming.side and o.qty > 0]
        opposite.sort(key=lambda o: o.price if incoming.side == 'BUY' else -o.price)
        fills = []
        for resting in opposite:
            crosses = (incoming.price >= resting.price if incoming.side == 'BUY'
                       else incoming.price <= resting.price)
            if not crosses or incoming.qty == 0:
                break
            qty = min(incoming.qty, resting.qty)
            incoming.qty -= qty
            resting.qty -= qty
            fills.append({'maker': resting.id, 'taker': incoming.id,
                          'qty': qty, 'price': resting.price})
        self.orders = [o for o in self.orders if o.qty]
        if incoming.qty:
            self.orders.append(incoming)
        return fills


def auction_candidates(buys, sells):
    """Volume-only LO demonstration; deliberately does NOT implement venue tie-breaks."""
    for price, qty in buys + sells:
        if type(price) is not int or type(qty) is not int or price <= 0 or qty <= 0:
            raise ValueError('Positive integer price/qty required')
    rows = []
    for p in sorted({p for p, _ in buys + sells}):
        demand = sum(q for price, q in buys if price >= p)
        supply = sum(q for price, q in sells if price <= p)
        rows.append({'price': p, 'demand': demand, 'supply': supply,
                     'executable': min(demand, supply)})
    best = max((r['executable'] for r in rows), default=0)
    candidates = [r['price'] for r in rows if best > 0 and r['executable'] == best]
    return {'rows': rows, 'max_volume': best, 'candidates': candidates,
            'needs_tiebreak': len(candidates) > 1, 'scope': 'VOLUME_ONLY_NOT_VENUE_RULES'}


class ReservationWallet:
    """In-memory concurrency/dedup lesson only. No persistence or settlement accounting."""
    def __init__(self, settled):
        if type(settled) is not int or settled < 0:
            raise ValueError('Invalid settled cash')
        self.settled = settled
        self.holds = {}
        self.requests = {}
        self._lock = Lock()

    @property
    def available(self):
        with self._lock:
            return self.settled - sum(self.holds.values())

    def reserve(self, key, amount):
        if not key or type(amount) is not int or amount <= 0:
            raise ValueError('Invalid request')
        with self._lock:
            if key in self.requests:
                old_amount, result = self.requests[key]
                if old_amount != amount:
                    raise ValueError('Idempotency payload conflict')
                return result
            accepted = self.settled - sum(self.holds.values()) >= amount
            self.requests[key] = (amount, accepted)
            if accepted:
                self.holds[key] = amount
            return accepted

    def release_confirmed(self, key):
        # Caller must have confirmed cancellation/rejection evidence. Timeout is not evidence.
        with self._lock:
            return self.holds.pop(key, 0)


def settlement_date(trade_date, days, holidays=frozenset()):
    """Calendar arithmetic only. Does not assert that settlement actually completed."""
    if type(days) is not int or days < 0:
        raise ValueError('Invalid day count')
    if trade_date.weekday() >= 5 or trade_date in holidays:
        raise ValueError('Trade date is not a business day in this lab calendar')
    result = trade_date
    while days:
        result += timedelta(days=1)
        if result.weekday() < 5 and result not in holidays:
            days -= 1
    return result


def reconcile(expected, actual):
    """Rows: id, qty, price. IDs assumed unique in a preselected venue/date scope."""
    def collect(rows):
        counts = Counter(r['id'] for r in rows)
        index = {}
        conflicts = set()
        for r in rows:
            if r['id'] in index and index[r['id']] != r:
                conflicts.add(r['id'])
            index.setdefault(r['id'], r)
        return index, sorted(k for k, n in counts.items() if n > 1), sorted(conflicts)
    left, dup_left, conflict_left = collect(expected)
    right, dup_right, conflict_right = collect(actual)
    return {
        'missing': sorted(left.keys() - right.keys()),
        'extra': sorted(right.keys() - left.keys()),
        'mismatched': sorted(k for k in left.keys() & right.keys()
                             if (left[k]['qty'], left[k]['price']) != (right[k]['qty'], right[k]['price'])),
        'duplicate_expected': dup_left, 'duplicate_actual': dup_right,
        'conflict_expected': conflict_left, 'conflict_actual': conflict_right,
    }


def demo():
    book = Book()
    for o in [Order('S1','SELL',25000,100),Order('S2','SELL',25000,200),Order('S3','SELL',25100,300)]:
        book.submit(o)
    fills = book.submit(Order('B1','BUY',25100,450))
    expected = [{'id':'E1','qty':100,'price':20000},{'id':'E2','qty':50,'price':20100}]
    result = {
        'notice':'Synthetic offline lesson; no venue connection or production certification',
        'fills':fills,
        'notional':sum(f['qty']*f['price'] for f in fills),
        'auction':auction_candidates([(100,200),(101,300),(102,100)],[(100,100),(101,300),(102,200)]),
        't_plus_2':settlement_date(date(2026,11,6),2).isoformat(),
        'reconciliation':reconcile(expected,[expected[0],expected[0]])
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    demo()
