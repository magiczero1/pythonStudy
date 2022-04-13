#http://www.tuku.com.cn/
import requests
import re
from lxml import etree
compile1 = re.compile('<img id="DataList1_ctl01_Image1" class="pic1" src="(?P<link>.*?)"style="border-width:0px;')
UA={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}
url = "http://www.tuku.com.cn/"
resp = requests.get(url,headers=UA)
result1 = compile1.finditer(resp.text)
for i in result1:
    print(i.group())

