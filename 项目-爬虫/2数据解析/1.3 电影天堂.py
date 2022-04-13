import requests as R
import re
url = "https://dytt89.com/"
resp=R.get(url,verify=0)#verify=0 去掉安全验证
resp.encoding="gb2312"#指定字符集，可通过网站中的charset找
print(resp.text)
obj = re.compile(r'')