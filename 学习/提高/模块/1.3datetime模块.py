import datetime as dt

print(dt.datetime.now())
print(dt.date(2020, 1, 1))  #创建一个日期
print(dt.time(12,16,9))     #创建一个时间
print(dt.datetime.now() + dt.timedelta(3)) #计算三天以后的时间