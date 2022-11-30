import os
import numpy
import threading
import queue
import time
from threading import Timer

class myThread (threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                filename=self.q.get()
                queueLock.release()
                try:
                    process_img(filename)
                except Exception as err:
                    print(filename)
                    print(err.__class__.__name__,err)
            else:
                queueLock.release()

def create_threads(file_list):
    global exitFlag,queueLock,workQueue,percentage,bar
    total_thread=5
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
    for k in file_list:
        workQueue.put(k)
    queueLock.release()

    # 等待队列清空
    while not workQueue.empty():
        #pass
        # 每隔0.5秒更新进度条
    	timer = Timer(0.5, update_progress)
    	timer.start()
    	timer.join()

    # 通知线程是时候退出
    exitFlag = 1
    # 修复最后90％~100％显不出来的bug
    percentage_difference=(100-percentage)/total_thread
    bar_difference=(width-bar)/total_thread
    # 等待所有线程完成
    for t in threads:
        t.join()
        percentage+=percentage_difference
        bar+=bar_difference
        print(f'[{"█"*int(round(bar))}{" "*(width-int(round(bar)))}] {int(round(percentage))}％',end='\r',flush=True)

def process_img(filename):
    global key,count
    with open(filename,'rb') as in_file:
        data=in_file.read()
        # 从文件头两个字节进行异或运算，判断图片类型
    imghead=[[0xff,0xd8,'jpg'],[0x47,0x49,'gif'],[0x89,0x50,'png']]
    
    for j in range(0,3):
        img_type=''
        if key is None:
            key=data[0]^imghead[j][0]
        if key==data[1]^imghead[j][1]:
            img_type=imghead[j][2]
            break
    if img_type=='':
        failure.append(filename)
    else:
        output_file=outputpath+'\\'+time.strftime('%Y%m%d_%H%M%S',time.localtime(os.path.getctime(filename)))+'.'+img_type
        with open(output_file,'wb') as out_file:
            out_file.write(bytearray(numpy.bitwise_xor(bytearray(data),key)))
        count+=1

def update_progress():
    global bar,percentage,count
    bar = int(width*count/total_number)
    percentage=int((count/total_number)*100)
    print(f'[{"█"*bar}{" "*(width-bar)}] {percentage}％',end='\r',flush=True)

if __name__=='__main__':
    dat_path=r'D:\Documents\WeChat Files\Scott373519\FileStorage\MsgAttach\8c8452efc6a908ce7e0c7803d32260bc\Image\2022-10'
    month=dat_path.split('\\')[-1]
    outputpath=f'd:\\decrypt\\{month}'
    if not os.path.exists(outputpath): os.makedirs(outputpath)
    exitFlag = 0  # 线程退出的标志
    queueLock = threading.Lock()
    workQueue = queue.Queue()
    dat_files=[]
    for i in os.listdir(dat_path):
        if os.path.splitext(i)[1]=='.dat':
            dat_files.append(dat_path+'\\'+i)
    total_number=len(dat_files)
    if total_number==0:
        print('该目录里没有.dat文件：',dat_path)
        exit()
    count=0  # 统计进度
    bar=0   # 画进度条的方格数
    percentage=0 # 进度条百分比
    width=70    # 进度条宽度
    key=None
    failure=[]
    now=time.time()
    create_threads(dat_files)
    print(f'耗时：{time.time()-now:.2f}秒。')
    if failure:
        with open('c:\\failure.txt','w',encoding='utf-8') as file:
            for i in failure:
                file.write(i+'\n')
        print('存在处理不了的.dat文件，已写入C:\\failure.txt文件里。')

