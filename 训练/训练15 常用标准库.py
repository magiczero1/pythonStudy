import sys
import time
import math

import urllib.request#互联网访问
print(sys.getsizeof(15))
'''
import schedule
def job():
    a=math.pi
    print("hhahahahaha----",a)
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
'''
import os #调用系统应用
path=os.getcwd()#获取当前目录
lst=os.listdir(path)#获取当前目录下的所有文件
for filename in lst:
    if filename.endswith(".py"):#找到当前目录下的py文件
        print(filename)