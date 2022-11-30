#import queue
import threading
import requests
from lxml import etree

def process_data(url):
    name_list=[]
    print ("Page:",url[-2:])
    res=se.get(url,headers=headers).text
    html=etree.HTML(res)
    name_list=html.xpath('//*[@id="results"]/li/a/text()')
    for i in range(len(name_list)):
        if 'GONGSI' in name_list[i] or 'ZH' in name_list[i] or 'SHAN' in name_list[i] or 'GUAN' in name_list[i]:
            continue
        name_list[i]=name_list[i].strip().title()
        file.write(name_list[i]+'\n')

outputfile=r'F:\Users\Administrator\Desktop\temp\UK海关数据买家.txt'

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',}
se = requests.session()
start_url='https://www.uktradeinfo.com/search/traders/?q=940549&t=Traders%3a%3acommodity-code&traders=Importers&year=2022&trader_name=&postcode=&county=&p='
startpage=1
lastpage=52
# 分页链接
linklist=[]
for pages in range(startpage,lastpage+1):
    linklist.append(start_url+str(pages))
file=open(outputfile,'a+',encoding='utf-8')
# 创建新线程
threadlist=[]
for i in linklist:
    thread_item=threading.Thread(target=process_data,args=[i])
    threadlist.append(thread_item)
# 分批进行，patch是每批多少线程
patch=30
total_threads=threadlist.__len__()
count=0
while count<total_threads:
	each_patch_start=count
	for j in range(patch):
		if count>=total_threads: break
		threadlist[count].start()
		count+=1
	each_patch_end=count
	for j in range(each_patch_start,each_patch_end):
		threadlist[j].join()

# 检查各个线程是否活着
while True:
	for i in threadlist:
		if not i.is_alive():
			total_threads-=1
	if total_threads<=0:
		break
file.close()
print ("退出主线程")
