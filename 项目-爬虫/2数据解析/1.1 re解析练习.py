import re
import requests as R
a=input("请输入你想搜索的内容：")
url="https://www.baidu.com/s?ie=UTF-8&wd={}".format(a)
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
resp=R.get(url,headers=UA)
with open("re_practice.html","w",encoding="utf-8") as rp:
    rp.write(resp.text)
print("okk!")