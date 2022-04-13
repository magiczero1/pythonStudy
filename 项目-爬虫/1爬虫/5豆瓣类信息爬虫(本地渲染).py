import requests
url="https://movie.douban.com/j/new_search_subjects?"
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
#重新封装参数,在抓包中找query string
param={
"sort": "U",
"range": "0,10",
"tags": "",
"start": 20,
"genres":"剧情"
}
resp=requests.get(url,params=param,headers=headers)
print(resp.request.url)#打印当前请求后的url
print(resp.json())#被反爬，一般使用UA进行处理
resp.close()