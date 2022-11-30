import requests
import time
url='https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=localCityNCOVDataList,diseaseh5Shelf'
data={}
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',}
res=requests.get(url,headers=headers).json()
data=res['data']['diseaseh5Shelf']['areaTree'][0]
print(f"\t\t国内新冠疫情统计数据\n\n资料来源：https://news.qq.com/zt2020/page/feiyan.htm\n\t\t{time.strftime('%Y年%m月%d日',time.localtime())}\t{time.strftime('%H:%M:%S',time.localtime())}\n{'-'*50}")
print("地区\t新增\t现有\t累计\t累计\t累计\n\t确诊\t确诊\t确诊\t治愈\t死亡")
print("-"*50)
for i in data['children']:
    print(f"{i['name']}\t{i['today']['confirm']}\t{i['total']['nowConfirm']}\t{i['total']['confirm']}\t{i['total']['heal']}\t{i['total']['dead']}")
print(f"\n合计\n{'-'*50}")
print(f"{data['name']}\t{data['today']['confirm']}\t{data['total']['nowConfirm']}\t{data['total']['confirm']}\t{data['total']['heal']}\t{data['total']['dead']}\n{'-'*50}")
