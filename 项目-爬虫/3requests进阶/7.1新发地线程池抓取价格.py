import requests as R
import re,time
import csv
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

list = []
comp1 = re.compile(r'''{"id":(?P<id>.*?),"prodName":"(?P<name>.*?)","prodCatid":.*?,"prodCat":(?P<type>.*?),"prodPcatid":.*?,"prodPcat":"","lowPrice":"(?P<lowprice>.*?)","highPrice":"(?P<highprice>.*?)","avgPrice":"(?P<avgprice>.*?)","''')
for num in range(50):
    data = {
        "current": num
    }
    resp = R.post("http://www.xinfadi.com.cn/getPriceData.html",headers=UA,data=data)
    ret = comp1.finditer(resp.text)
    for i in ret:
        list.append(i.group("name","avgprice"))
    for j in range(len(list)):
        with open("vegtable.csv","a",encoding="utf-8") as file:
            file.write(str(list[j]))
            file.write("\n")
resp.close()
print("ok")