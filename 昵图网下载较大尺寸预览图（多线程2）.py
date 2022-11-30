## 线程优先级队列（ Queue）
## Python 的 Queue 模块中提供了同步的、线程安全的队列类，
## 包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，
## 和优先级队列 PriorityQueue。
## 这些队列都实现了锁原语，能够在多线程中直接使用，
## 可以使用队列来实现线程间的同步。

import queue
import threading
import requests
import re
import os

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print (f"开启线程：{self.name}")
        process_data(self.name, self.q)
        print (f"退出线程：{self.name}")

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            url = q.get()
            queueLock.release()
            # 打开缩略图链接，每个线程下载一个页面的所有大图
            small_list=[]
            res=se.get(url,headers=headers).text
            small_list=re.findall('data-original="(.*?)"',res)
            print (f"线程{threadName}下载{len(small_list)}个图片……")
            big_url=''
            # 记录是否有重复文件
            repeat_file=0
            for i in small_list:
                split_list=i.split('/')
                big_url='https://pic.ntimg.cn/file/'+split_list[4]+'/'+split_list[5][:-5]+'2.jpg'
                filepath=outputpath+'\\'+split_list[5][:-5]+'2.jpg'
                if os.path.lexists(filepath):   # 重复的文件不用下载
                    repeat_file+=1
                    continue
                f=open(filepath,'wb')
                c=se.get(big_url,headers=headers)
                f.write(c.content)
                f.close()
            if repeat_file>0: print (f"线程{threadName}发现{repeat_file}个重复的图片。")
        else:
            queueLock.release()


outputpath=r'F:\Users\Administrator\Desktop\temp\七夕'
if not os.path.exists(outputpath): os.mkdir(outputpath)

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',}
se = requests.session()
start_url='https://soso.nipic.com/?q=%E4%B8%83%E5%A4%95&g=1&or=0&y=60&page='
startpage=5
lastpage=14
# 定义10线程
threadList = range(10)
# 缩略图的页面链接
linkList=[]
for pages in range(startpage,lastpage+1):
        linkList.append(start_url+str(pages))
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 把缩略图的页面链接填充到队列
queueLock.acquire()
for k in linkList:
    workQueue.put(k)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
