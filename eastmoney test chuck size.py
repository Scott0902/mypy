import os
import json
import requests

alist=['002487','000683','603982','603619','600989','000821','603396','002459','603398','605133','002903','000519','002101','603690','002335','002885','603138','002432','600546','603520','601126','002326','600702','002245','002709','002363','002268','002922','002837','003022']
stocklist=[]
serverid='20'
list_len=len(alist)
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Safari/537.36"}
ff=['2','12','14','18','3','22','62','109','110','127']
ffstr=''
for i in ff: ffstr+='f'+i+','
ffstr=ffstr[:-1]
for i in range(list_len):
    stocklist=alist[0:i+1]
    secids='1.'+stocklist[0] if stocklist[0][:2]=='60' else '0.'+stocklist[0]
    if len(stocklist)>1:
        for i in stocklist[1:]:
            secids+=','+('1.'+i if i[:2]=='60' else '0.'+i)
    elif len(stocklist)==0: 
        print('股票代码列表为空，退出程序。')
        exit()
    url=f'https://{serverid}.push2.eastmoney.com/api/qt/ulist/sse?pi=0&pz={list_len}&secids={secids}&fields={ffstr}'
    r=requests.get(url,headers=headers,stream=True)
    for j in r.iter_content(chunk_size=10240):
        if j:
            break
    j=j.decode().strip()
    print('Length:',len(j))
## 结果分析，股票push信息返回的结果长度随着stocklist长度而增加
## 一个股票的信息长度216字节，每增加一个股票，信息长度增加125~130字节
## 因此设定初始chunk_size为256字节，每增加一个股票，chunk_size长度增加128字节
## chunk_size=256+(len(stocklist)-1)*128