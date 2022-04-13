#1.找到加密的参数
#2.想办法吧参数按照网易的规则进行加密，调用window.asrsea之后，将params => encText，encSecKey => encSecKey
#3.重新请求，拿到数据
from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="#请求地址
data = {
    "csrf_token":"",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1909021556",
    "threadId": "R_SO_4_1909021556"
}#data 拿到真实参数,此时数据类型为字典
e = "010001"
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'Xov71NjgEy5aAP5g'#encSecKey是通过i来进行加密的，如果i定死，那么encSecKey也是定值

def encSecKey():
    return "c85fa62515b579e673d445056ddf57c5dce1d595a8992888594b26003f094c0846e0633af6d656e27b433f47afcdb582dd231151fd78a35a7629b31f7d61f5e9f728aea4e70c94a6e04ca29be63d009aa9dbf48a2cd8a5f5807be26b0706eae8c6a96593ba2b87a68113846b38a52e6619f9ec84eb98a20f0163ccdbdee394c6"

def get_params(data):#data默认收到的是字符串，需要转化
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second   #返回的就是params

def to_16(data):
    pad = 16 - len(data)%16
    data  +=  chr(pad)*pad
    return data
def enc_params(data,key):#加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)#制作加密器
    bs = aes.encrypt(data.encode("utf-8"))#使用加密器对data进行加密，封装进bs.     注意加密的长度必须是16的倍数
    return str(b64encode(bs),"utf-8")#先用b64对bs进行utf-8编码，然后转化成str

resp = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":encSecKey()
})
print(resp.text)