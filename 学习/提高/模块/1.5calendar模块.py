import calendar

print(calendar.firstweekday())  #每周的起始是周几  0-6
calendar.setfirstweekday(6)     #设置起始日
print(calendar.calendar(2022))
print(calendar.month(2022,3))