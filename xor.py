import time
import numpy
# 生成一串5MB的随机字节，模拟一个5MB的二进制文件
aa=bytes(numpy.uint8(numpy.random.randint(0, 256, 5*1024*1024)))
# 参与异或运算的参数
num=88

# 方法一：逐个字节地进行异或运算并写入文件
def test1():
    now=time.time()
    with open('test1.dat','wb') as file:
        for i in aa:
            file.write(bytes([i^num]))
    print(f'方法一用时：{time.time()-now:.2f}s')

# 方法二：用numpy进行整体异或运算，最后才写入文件
def test2():
    now=time.time()
    bb=bytearray(numpy.bitwise_xor(bytearray(aa),num))
    with open('test2.dat','wb') as file:
        file.write(bb)
    print(f'方法二用时：{time.time()-now:.2f}s')
    
if __name__=='__main__':
    test1()
    test2()