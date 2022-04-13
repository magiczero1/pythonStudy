import re,requests
url = "https://dytt89.com"
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
resp = requests.get(url,verify=0,headers=UA)
resp.encoding = "gbk"
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<web_movie_id>.*?)</ul>',re.S)#第一个页面正则，获取movie_id
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)#抓取子页面正则，获取子页面中的href
obj3 = re.compile(r'<tbody>.*?<a href="(?P<magnet>.*?)">',re.S)#子页面内容正则，获取magnet
content1 = obj1.finditer(resp.text)#抓取第一个页面源码,形成迭代器
content2_href = []#提前准备好空列表
for it in content1:
    web_movie_id = it.group('web_movie_id')  #利用group输出迭代器内容，获取所有movie_id
    #提取子页面内容
    content2 = obj2.finditer(web_movie_id)#抓取页面中的href，形成content2
    for it2 in content2:
        href = url+it2.group("href")#连接原网址和movie_id，形成完整的链接
        content2_href.append(href) #将所有链接放入content2_href列表中
with open("movie_magnet.txt","w",encoding="utf-8") as mm:
    for it3 in content2_href:#从content2_href中遍历链接
        resp2 = requests.get(it3,verify=0)#打开每一个content2_href中的链接，并存入resp2
        resp2.encoding = "gbk"#对每个打开的连接以"gbk"格式编码，兼容gb2312
        content3 = obj3.search(resp2.text)
        mm.write(content3.group("magnet"))
        mm.write("\n")


