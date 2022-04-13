import requests
query=input("请输入你想搜索的内容：")
url = f"https://www.sogou.com/web?query={query}"
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}#调用UA
resp = requests.get(url,headers=headers)
#print(resp.text)
with open("my1stspiders.html", "w") as m1:
    m1.write(resp.text)
print("ok")
resp.close()