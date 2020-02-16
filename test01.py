import os
import re
import time
import fibo
import random
import tkinter

'''file = open('C://Users/A/Desktop/test.txt','w+')
file.write('hello')
file.close()
创建文件并写入'''
'''os.remove('C://Users/A/Desktop/变态超爆传奇.lnk')
删除文件'''


'''file = open("E:/test.txt","a+")
file.write('+')
file.close()
x = os.path.getsize("E:/test.txt")
print(x)

file = open("E:/timer.txt","a+")
file.write(str(time.ctime())+'\n'+'+')
file.close()
上面创建并写入并读取大小
下面记录时间'''

'''if __name__=='__main__'
若当前函数为主函数（不是被import的）就返回True
代码规范性'''

'''file = open('C://Users/A/record.txt','a+')
a = 123
s = str(a).rjust(5, )
file.write(s + '\n')
file.close()
count = os.path.getsize('C://Users/A/record.txt')
print(count)
str.rjust右对齐      ljuust左对齐'''

a='y'
b=input()
print(a==b)