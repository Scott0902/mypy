import os
path=r'D:\Documents\WeChat Files\Scott373519\FileStorage\Image\2022-06'
dir_content=os.listdir(path)
imghead=[[0xff,0xd8,'jpg'],[0x89,0x50,'png'],[0x47,0x49,'gif']]
for i in dir_content:
    with open(os.path.join(path,i),'rb') as file:
        data=file.read(2)
        for j in range(0,3):
            img_type=''
            key=data[0]^imghead[j][0]
            if key==data[1]^imghead[j][1]:
                img_type=imghead[j][2]
                break
        if img_type=='':
            print('无法判断该.dat文件类型：',i)
    if img_type!='':print(i,img_type)

        
        
