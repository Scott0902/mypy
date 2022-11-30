## FOB网站有反爬虫机制，不能大批量获取信息

import requests
import re
import csv
import threading
import queue
import time

class myThread (threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                arg=self.q.get()
                queueLock.release()
                try:
                    result = requests.get('https://ip.seeip.org/jsonip?',proxies={'http': arg, 'https': arg},timeout=5)
                    valid_ips.append(arg)
                except Exception as err:
                    #print(err.__class__.__name__,err)
                    print(f"{arg} invalid")
            else:
                queueLock.release()

def create_threads(proxy_list):
    global exitFlag,queueLock,workQueue
    total_thread=50
    queueLock = threading.Lock()
    workQueue = queue.Queue()
    threads = []
    # 创建新线程
    for t in range(total_thread):
        thread=myThread(workQueue)
        thread.daemon=False
        thread.start()
        threads.append(thread)
        
    # 把链接填充到队列
    queueLock.acquire()
    for k in proxy_list:
        workQueue.put(k)
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是时候退出
    exitFlag = 1
    # 等待所有线程完成
    for t in threads: t.join()

def get_proxy_list():
    try:
        res=requests.get("https://free-proxy-list.net",headers=headers,proxies=init_proxy,timeout=5)
        if res.status_code==200:
            proxy_ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)  #「\d+」代表數字一個位數以上
            print('Received proxy lists.')
            return proxy_ips
    except:
        print('Open proxy website error.')

def load_url_list():
    urllist=[]
    with open(r'F:\Users\Administrator\Desktop\temp\fob uk lighting url list.txt','r',encoding='gbk') as file:
        urllist=file.read().splitlines()


if __name__=='__main__':
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',}
    init_proxy={'http':'127.0.0.1:7890','https':'127.0.0.1:7890'}
    failure=[]
    valid_ips=[]
    proxy_list=[]
    count=0
    exitFlag = 0
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)

#    csvfile=open(r'F:\Users\Administrator\Desktop\temp\fob uk list.csv','w',encoding='gbk', newline="")
#    writer=csv.writer(csvfile)
#    writer.writerow(['Company','Industry','About','Product','Phone','Fax','Address','Email','Emails'])
#    csvfile.close()
#    print('Finished.')
    proxy_list=get_proxy_list()
    if len(proxy_list)>0:
        create_threads(proxy_list)
        with open(f'c:\\proxy_{time.strftime("%Y%m%D%H%M%S")}.txt','w',encoding='gbk') as file:
            for i in valid_ips:
                file.write(i+'\n')
