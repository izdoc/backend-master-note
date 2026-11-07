"""Regenerate Markdown navigation using only Python standard library."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={
'00-start-here':'Lộ trình và cách học','01-market-foundations':'Nền tảng thị trường',
'02-exchange-operations':'Vận hành sở giao dịch','03-trading-and-matching':'Giao dịch và khớp lệnh',
'04-broker-departments':'Nghiệp vụ công ty chứng khoán','05-connectivity':'Kết nối thị trường',
'06-market-data':'Bảng điện và dữ liệu thị trường','07-post-trade':'Sau giao dịch',
'08-risk-and-compliance':'Rủi ro và tuân thủ','09-solution-architecture':'Kiến trúc giải pháp',
'10-operations-and-security':'Vận hành và bảo mật','11-leadership-and-governance':'Quản trị và giám đốc nghiệp vụ',
'12-workshops':'Workshop và đánh giá','13-reference':'Tra cứu và nguồn'}
ORDER={
'01-market-foundations':['ecosystem','products','accounts-and-balances','derivatives-and-bonds'],
'03-trading-and-matching':['order-types','continuous-matching','auction-and-negotiated','order-lifecycle'],
'04-broker-departments':['operating-model','customer-and-cash','margin-and-treasury','institutional-business'],
'07-post-trade':['clearing-settlement','corporate-actions','ledger-reconciliation'],
'09-solution-architecture':['reference-architecture','data-api-events','dotnet-sql-design'],
'12-workshops':['workshops','assessment','capstone'],
'13-reference':['glossary','sources','regulatory-watch']}
def main():
    index=['# Mục lục toàn bộ wiki','', '[Trang đầu](README.md)','']
    catalog=[]
    for folder,title in CATEGORIES.items():
        path=ROOT/'docs'/folder
        rank={name:i for i,name in enumerate(ORDER.get(folder,[]))}
        pages=sorted((p for p in path.glob('*.md') if p.name!='README.md'),key=lambda p:(rank.get(p.stem,100),p.name))
        local=[f'# {title}','','[Trang đầu](../../README.md) · [Mục lục toàn bộ](../../INDEX.md)','']
        index.extend([f'## {folder[:2]}. {title}',''])
        items=[]
        for p in pages:
            heading=next(line[2:] for line in p.read_text().splitlines() if line.startswith('# '))
            local.append(f'- [{heading}]({p.name})')
            index.append(f'- [{heading}]({p.relative_to(ROOT).as_posix()})')
            items.append({'title':heading,'path':p.relative_to(ROOT).as_posix()})
        index.append('')
        path.joinpath('README.md').write_text('\n'.join(local)+'\n')
        catalog.append({'category':folder,'title':title,'pages':items})
    ROOT.joinpath('INDEX.md').write_text('\n'.join(index))
    ROOT.joinpath('config/catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    print(f'Indexed {sum(len(c["pages"]) for c in catalog)} pages in {len(catalog)} categories')
if __name__=='__main__':main()
