import random
import os
import time
import json
import requests
stocklist=['002487','000683','600989','603619','603690']
secids='1.'+stocklist[0] if stocklist[0][:2]=='60' else '0.'+stocklist[0]
if len(stocklist)>1:
    for i in stocklist[1:]:
        secids+=','+('1.'+i if i[:2]=='60' else '0.'+i)
elif len(stocklist)==0: 
    print('股票代码列表为空，退出程序。')
    exit()
os.system('')
serverid='20'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36"}
ff=['36','109','110','127','372']
ffstr=''
fff=''
for i in ff: ffstr+='f'+i+','
ffstr=ffstr[:-1]
url=f'https://{serverid}.push2.eastmoney.com/api/qt/ulist/sse?pi=0&secids={secids}&fields={ffstr}'
while 1:
    try:
        r=requests.get(url,headers=headers,stream=True)
        for i in r.iter_content(chunk_size=2048):
            if i:
                break
        i=i.decode().strip()
        d=json.loads(i[6:])['data']['diff']
        #lastday=d['f18']/100
        print(f'\x1b[2J\x1b[0;0H',end='')
        for i in ff:print(f'f{i}\t',end='')
        print('\n')
        for i in d:
            for k in ff:
                fff='f'+k
                try:
                    print(f"{d[i][fff]}\t",end='')
                except KeyError:
                    print('N/A\t',end='')
            print('\n')
        time.sleep(2)
    except Exception as err:
        print(err)
        #serverid=str(random.randint(10,100))
