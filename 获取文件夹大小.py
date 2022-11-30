import os
 
def GetDirSize(dir):
   size = 0
   for root, dirs, files in os.walk(dir):
      size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
   return size

path=r'D:\Documents\WeChat Files\Scott373519\FileStorage\MsgAttach'
dir_content=os.listdir(path)
dir_num=len(dir_content)
dir_size=[]
count=0
for i in dir_content:
    print(f'正在统计微信图片缓存各个子目录的大小…… {int(count/dir_num*100)}％',end='\r',flush=True)
    dir_size.append([i,GetDirSize(os.path.join(path,i))/1048576])
    count+=1
#按大小排序
dir_size=sorted(dir_size,key=lambda x: x[1],reverse=True)
count=0
filter_size=100
filter_dir=[]
print('\n超过{filter_size}MB的子目录有：')
for i in dir_size:
    if i[1]>=filter_size:
        print(f'（{count+1}）{i[0]}\t{i[1]:.2f} MB')
        filter_dir.append(os.path.join(path,i[0]))
        count+=1

aa=input('请输入一个序号：').strip()
if aa.isdigit():
    aa=int(aa)
    if aa<0 and aa>len(filter_dir)-1:
        print('输入有误！')
        exit()
else:
    print('输入有误！')
    exit()
print(f'开始处理{filter_dir[aa]}目录内的.dat文件')

