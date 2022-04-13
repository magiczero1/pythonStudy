from lxml import etree
import time,requests
url = "https://umei.cc/bizhitupian/meinvbizhi/yangyanmeinv.htm"
url1 = "https://umei.cc"
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
resp = requests.get(url,headers=UA)
resp.encoding = "utf-8"
html = etree.HTML(resp.text)
divs = html.xpath(r"//*/div[2]/div[7]/ul/li/a/@href")
for div in divs:
    url2 = url1 + div
    img = requests.get(url2)
    img_name = div.split("/")[-1]
    with open("img2/"+img_name,"wb") as img_f:
        img_f.write(img.content)
    print("下载好了一张图片：",img_name)
resp.close()