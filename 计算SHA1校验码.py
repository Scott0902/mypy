from hashlib import sha1
import sys

def calc_sha1(file):
    sha1Obj = sha1()
    with open(file, 'rb') as f:
        while True:
        	# 设置10M读取缓存，防止内存溢出
            buf = f.read(1 * 1024 * 1024)
            if buf:
                sha1Obj.update(buf)
                print(len(buf))
            else:
                break
    print(sha1Obj.hexdigest())


if __name__ == '__main__':
    calc_sha1(r'D:\Documents\WeChat Files\Scott373519\FileStorage\MsgAttach\8c8452efc6a908ce7e0c7803d32260bc\Image\2022-09\7c5ef7ce581bbfa344db968a30bbdd03.jpg')
