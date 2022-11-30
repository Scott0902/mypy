import random
import time
import json
import requests
stocklist=['002487']
secids='1.'+stocklist[0] if stocklist[0][:2]=='60' else '0.'+stocklist[0]
if len(stocklist)>1:
    for i in stocklist[1:]:
        secids+=','+('1.'+i if i[:2]=='60' else '0.'+i)
elif len(stocklist)==0: 
    print('股票代码列表为空，退出程序。')
    exit()
serverid=str(random.randint(10,100))
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36"}
for kk in range(300,500,100):
    ff=range(kk,kk+100)
    ffstr=''
    for i in ff:
        ffstr+='f'+str(i)+','
    ffstr=ffstr[:-1]
    url=f'https://{serverid}.push2.eastmoney.com/api/qt/ulist/sse?pi=0&secids={secids}&fields={ffstr}'
    r=requests.get(url,headers=headers,stream=True)
    for i in r.iter_content(chunk_size=10240):
        if i:
            break
    i=i.decode().strip()
    d=json.loads(i[6:])['data']['diff']
    for i in d:
        for k in ff:
            fff='f'+str(k)
            try:
                print(f"{fff}: {d[i][fff]}\t")
            except KeyError:
                #print('N/A\t',end='')
                pass
        print('\n')
