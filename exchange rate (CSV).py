import requests
import csv
from lxml import etree

def get_exchange_rate():
    url='https://www.boc.cn/sourcedb/whpj/'
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',}
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    html=etree.HTML(res.text)
    title=html.xpath('//table/tr/th/text()')
    writer.writerow(title)
    for i in range(2,29):
        rates=[]
        for j in range(1,9):
            if len(html.xpath(f'//table/tr[{i}]/td[{j}]/text()'))==0:
                rates.append('')
            else:
                rates.append(html.xpath(f'//table/tr[{i}]/td[{j}]/text()')[0])
        writer.writerow(rates)

if __name__=='__main__':
    outputfile='c:\\exchange rate.csv'
    csvfile=open(outputfile,'w',encoding='gbk', newline="")
    writer=csv.writer(csvfile)
    get_exchange_rate()
    csvfile.close()