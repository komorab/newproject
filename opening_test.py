#to delete a target file & count the times of opening
#2020-2-10

import os
import time
import shutil

def opening_count():
    "to record the times of opening"
    file = open('C://Users/A/record.txt', 'a+')
    file.write(str(time.ctime()))#record the time of opening
    file.close()
    count = os.path.getsize('C://Users/A/record.txt')
    count += 8
    count /= 32
    file = open('C://Users/A/record.txt', 'a+')
    s_time = str(count).rjust(6, )
    file.write( s_time + '\n')
    file.close()

if __name__=='__main__':
    opening_count()
    if os.path.exists('C://Users/A/Desktop/变态超爆传奇.lnk'):
        os.remove('C://Users/A/Desktop/变态超爆传奇.lnk')
    if os.path.exists('C://Users/A/Desktop/逆天回收+7777亿.lnk'):
        os.remove('C://Users/A/Desktop/逆天回收+7777亿.lnk')
    if os.path.exists('C://User/A/AppData/Local/CzPolicySvc'):
        shutil.rmtree('C://Users/A/AppData/Local/CzPolicySvc')