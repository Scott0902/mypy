import os
def dir_s(path,ext):
   ll=[]
   if ext[0]=='*': ext=ext[1:]
   if ext[-1:]=='*':
       extlen=len(ext)
       ext=ext[:-1]
       for root, dirs, files in os.walk(path):
            for name in files:
                if os.path.splitext(name)[1][:extlen-1]==ext:
                    ll.append(os.path.join(root,name))
   else:
       for root, dirs, files in os.walk(path):
            for name in files:
                if os.path.splitext(name)[1]==ext:
                    ll.append(os.path.join(root,name))
   return ll

def dir_b(path,ext):
   ll=[]
   if ext[0]=='*': ext=ext[1:]
   if ext[-1:]=='*':
       extlen=len(ext)
       ext=ext[:-1]
       for name in os.listdir(path):
           if os.path.splitext(name)[1][:extlen-1]==ext:
               ll.append(os.path.join(path,name))
   else:
        for name in os.listdir(path):
            if os.path.splitext(name)[1]==ext:
                ll.append(os.path.join(path,name))
   return ll
   
if __name__=='__main__':
    path=r'D:\Scott'
    ext='*.*'
    print(f"{'='*60}\n模拟DOS命令：dir /b {ext}\n")
    filelist1=dir_b(path,ext)
    for i in filelist1:
        print(i)
    print(f'合计：{len(filelist1)}个文件。')
    
    print(f"\n{'='*60}\n模拟DOS命令：dir /b /s {ext}\n")
    filelist2=dir_s(path,ext)
    for i in filelist2:
        print(i)
    print(f'合计：{len(filelist2)}个文件。')
