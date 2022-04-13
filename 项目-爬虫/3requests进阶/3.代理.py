#proxies
import requests as R

url = "https://www.baidu.com/"
proxies = {
    "https":"https://121.232.148.241:9000"
}
resp = R.get(url,proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)