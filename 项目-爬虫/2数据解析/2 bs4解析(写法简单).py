import requests,time
from bs4 import BeautifulSoup
#coding = "utf-8"
url = "https://umei.cc/weimeitupian/"
url1 = "https://umei.cc"
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
resp = requests.get(url,headers=UA)
resp.encoding = "utf-8"
#1.把resp得到的页面数据交给BeautifulSoup处理为bs对象
page1 = BeautifulSoup(resp.text,"html.parser")#指定html解析器，避免报错
#2.利用find对数据进行查找
#find(标签，属性=值) 找到第一个值就返回
#find_all 找全部的对应值
img_url_1 = page1.find("div",class_="TypeList").findAll("a")#用div定位页面位置，继续向下找a标签
for it in img_url_1:
    link = url1+it.get("href")#直接通过get拿href标签的数据，相比正则简单很多。
    resp2 = requests.get(link,headers=UA)
    resp2.encoding = "utf-8"
    page2 = BeautifulSoup(resp2.text,"html.parser")
    p = page2.find("p",align="center")
    img_1 = p.find("img")
    src =img_1.get("src")#取所有链接，返回的是字符串
    img_resp = requests.get(src,headers=UA)
    img_resp.content #取img_resp中的所有字节内容
    img_name = src.split("/")[-1]#将最后一个/后的内容作为文件名
    with open("img/"+img_name,"wb") as img_file:#wb是写入二进制
        img_file.write(img_resp.content)    #这种写法的问题是在于下载的图片默认与爬虫文件在同一文件夹下。利用"img/"+写入指定路径
    print("下载好了一张高清无码图片",img_name)
    time.sleep(2)
print("全部搞定")

