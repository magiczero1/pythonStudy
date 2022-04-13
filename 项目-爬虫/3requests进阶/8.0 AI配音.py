import requests as R
import re,datetime

day = datetime.datetime.now().day
print(day)


def AIvoice(word):
    url = "https://api.houzi8.com/weapi/tts/index-v2"

    UA={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "cookie":"track_id=805ba60e9fc9783f117de4aad654fcccbb851810f05797308fdf5fcf5919a3e1a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A55%3A%22d593709dc43c2d3fee619e2dac97cf52620b6a3e32ae99.37038398%22%3B%7D; user_source=938d6df6cf78cfa92ec9f3560e481be78db15c03543dab8010399687e82068b9a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22user_source%22%3Bi%3A1%3Bi%3A1%3B%7D; user_source_permanent=c94a58d3f3c9ae2a4357f23e9a97df55f56d3d6833b5d140506d2b3ded7b7320a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22user_source_permanent%22%3Bi%3A1%3Bi%3A1%3B%7D; Hm_lvt_bb1a215c22b753f9361786dbc9433727=1644915262; Qs_lvt_396365=1644915262; todayViewMark=869ad589fae6c88a6771e92dcd4c6244ecb5a7f270c1b784ad38801ba6646923a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22todayViewMark%22%3Bi%3A1%3Bi%3A1%3B%7D; __root_domain_v=.houzi8.com; _qddaz=QD.361044915263194; loginRedirectUrl=https://houzi8.com/AIVoice/editor; YPSSESSION=j7sqjabv4a9km2akp77u1hgvfp; _identity=aca9c885dd82756f590f577ffb900446b02a96d6fea440703a655f4a60fbe8cda%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A21%3A%22%5B609769%2Cnull%2C2592000%5D%22%3B%7D; _csrf=d64cb6099556fd943e375343952941ccddf4b625233a06d76df2868673a8672aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22JR3mmGIkpCnuNytC0ErKkf0pIg3x7geF%22%3B%7D; Hm_lpvt_bb1a215c22b753f9361786dbc9433727=1644915320; Qs_pv_396365=4540699340158035000%2C98396425100253680%2C571853325870349500"        }
    textData = {
        'text': word,
        'vcn': 'jielidou',
        'fun': 'aliLongTextSpeech',
        'speed': '0',
        'country': 'zh'
    }

    resp = R.post(url,data=textData,headers=UA)

    obj = re.compile(r'"stat":1,"msg":"操作成功","data":{"tts_id":.*?,"audio_url":".*?/(?P<link>.*?)"}')

    links = obj.finditer(resp.text)

    for it in links:
        link1 = it.group("link")
        finallink = link1[-36:]
    trueLink = r"https://img.houzi8.com/tc_tts_audio/2022/02/%d/"%day + finallink
    return trueLink

content = input("请输入祝福语：")
voice = R.get(AIvoice(content)).content
name = input("请输入文件名：")

with open(f"/Users/mac/Desktop/{name}.mp3","wb") as file:
    file.write(voice)
    print("ok")