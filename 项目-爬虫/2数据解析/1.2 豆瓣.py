import requests as R
import re
import csv#以逗号做分割
url="https://movie.douban.com/top250"
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
resp = R.get(url,headers=UA)
page_content=resp.text
obj = re.compile(r'<li>.*?<span class="title">(?P<movie_name>.*?)</span>.*?<p class="">.*?'
                 r'<br>(?P<year>.*?)&nbsp',re.S)
result = obj.finditer(page_content)
with open("movie_list.csv","w",encoding="utf-8") as f:
    csvwriter=csv.writer(f)
    for it in result:
    #写文件时整理成字典格式
    #print("《{0}》{1}".format(it.group("movie_name"),it.group("year").strip()))
        dic = it.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.valuses())
print("okk")