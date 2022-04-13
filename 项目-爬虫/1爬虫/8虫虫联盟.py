#虫虫联盟
import requests
from lxml import etree

UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
try:
    for i in range(1096033,1096050):
        url = "https://www.ivsky.com/tupian/wuyucun_v67365/pic_%d.html"%i
        imgname = "%d.jpg"%i
        resp = requests.get(url,headers=UA)
        resp.encoding = "utf-8"
        html1 = etree.HTML(resp.text)
        href = html1.xpath('//*/img[@id="imgis"]/@src')
        href1 = str(href)[4:-2]
        img = requests.get("https://"+href1)

        with open("img3/"+imgname,"wb") as img_f:
            img_f.write(img.content)
            print("成功下载一张图片")
except:
    print("所有图片下载完成")