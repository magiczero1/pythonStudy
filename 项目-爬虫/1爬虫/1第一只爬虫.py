from urllib.request import urlopen
url="https://www.bilibili.com/"
resp=urlopen(url)
with open("bilili.html", "w") as f:
    f.write(resp.read().decode("utf-8"))#将整个网页源代码以utf-8的方式写入f
print("over")