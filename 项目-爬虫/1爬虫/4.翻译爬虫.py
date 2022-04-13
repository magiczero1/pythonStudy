import requests as R
url = "https://fanyi.baidu.com/sug"
word = "black"
while True:
    data = {"kw": word}   #传一个字典
    resp = R.post(url,data=data)#告诉计算机，我要进到百度翻译里
    a = resp.json()  #json是()一个方法     调用json方法获取信息
    a = str(a)
    '''with open("word.txt","a",encoding="utf-8") as file:
        file.writelines(a+"\n")'''
    print(a)
resp.json()

