import requests as R
import re
for i in range(1):

    url1 = "https://gz.meituan.com/xiuxianyule/c52/pn2/" #店铺列表

    UA={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        "Cookie":'uuid=8f614eb99ed843718e50.1649045155.1.0.0; mtcdn=K; userTicket=ZtndGbNqcFspeORhrXYdFgDtbrNzYgGQefbaeMIX; _yoda_verify_resp=7x5SbXjBq2aRK82jQxRNs1wQYTR2CwObYQcvbUZSNeTO55JtCHH0NLixD8zUdUN60zZiYdoKyyi1cLi7Ej%2BpBBqcJLtrYtbMxWdECqlBBjcpX55vwTJ6O01PxsfBrMZ5Hwl0bO84aAQtnmhVR2SFn3EZ3Mrytl3mNLjL%2FloU8FX1CUnPKY%2BX5DUs%2B%2FIU0r2jIKyrAdkRj3oL%2B%2Fa6WBYNrtx%2F3DKh0DWzM82hozVPWqQRRbSW0Jiw0%2FMywZBMUnuL9VDDMiZXkdQ%2B1ALSpjDjiZGjlI153ZWAAgVei6SYTMYijqVu9bW2pptKfvp5NdjInPGk7JjSHyCxf4ydp0wUxHsZooGFsR%2FH6XwfsMOy4s2X307JixaLspQ2U3Skd%2B%2Fu; _yoda_verify_rid=14f7c6925381902c; u=299388693; n=WAI715253631; lt=Ireov25cxE6UGaspgKVsdBQQ7OoAAAAAQREAAAZ7wp0enYD35tlIhACaRLGuMGI1yA4IHkSbZ-JIY6I-86r9AgBa6Xb5euVsW9qxQg; mt_c_token=Ireov25cxE6UGaspgKVsdBQQ7OoAAAAAQREAAAZ7wp0enYD35tlIhACaRLGuMGI1yA4IHkSbZ-JIY6I-86r9AgBa6Xb5euVsW9qxQg; token=Ireov25cxE6UGaspgKVsdBQQ7OoAAAAAQREAAAZ7wp0enYD35tlIhACaRLGuMGI1yA4IHkSbZ-JIY6I-86r9AgBa6Xb5euVsW9qxQg; token2=Ireov25cxE6UGaspgKVsdBQQ7OoAAAAAQREAAAZ7wp0enYD35tlIhACaRLGuMGI1yA4IHkSbZ-JIY6I-86r9AgBa6Xb5euVsW9qxQg; unc=WAI715253631; ci=20; rvct=20%2C83; __mta=45937307.1649060982977.1649060982977.1649060982977.1; firstTime=1649061302763; _lxsdk_s=17ff3a67ad3-877-f63-0f4%7C%7C33'
    }

    #获取商家链接
    obj = re.compile('<div class="list-item-desc-top"><a href="//(?P<link_web>.*?)" target=.*?clearfix">',re.S)

    resp = R.get(url1,headers=UA)
    content = resp.text
    print(content)
    content1 = obj.finditer(content)
    links_list = []

    for link in content1:
        links = link.group("link_web")
        links = "https://"+links
        print(links)
        links_list.append(links)

    for web in links_list:

        #店铺名、地址、手机号
        url2 = web
        obj1 = re.compile(r'{".*?"shopName":"(?P<store_name>.*?)","score".*?"address":"(?P<address>.*?)","phone":"(?P<phone>.*?)",',re.S)

        content = R.get(url2,headers=UA)
        content1 = obj1.finditer(content.text)
        message = []
        message_list = []
        for it in content1:
            store_name = it.group('store_name')
            address = it.group('address')
            phone = it.group('phone')
            message.append("店名："+store_name)
            message.append("店铺地址："+address)
            message.append("联系方式："+phone)

        message_list.append(message)
        with open("mtcj.csv","a",encoding="utf-8") as file:
            file.write(str(message))
            file.write("\n")
print("ok")