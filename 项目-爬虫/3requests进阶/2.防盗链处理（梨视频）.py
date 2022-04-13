#控制台中能看到资源链接，源代码中看不到
#抓包后得到的是假链接
#假链接https://video.pearvideo.com/mp4/third/20211230/1641283976397-11320310-135629-hd.mp4 时间戳替换为真实id
#真链接https://video.pearvideo.com/mp4/third/20211230/cont-1748940-11320310-135629-hd.mp4
import requests
#访问原始页面，获取cont-id
url = "https://www.pearvideo.com/video_1749160"
UA={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intekl Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Referer":url
}
contID = url.split('_')[-1]
#视频请求页面，获取json，拿到src
videoStauts = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.11034971415302364"
resp = requests.get(videoStauts,headers=UA)#UA中加入Referer请求头
dic = resp.json()
srcurl = dic['videoInfo']['videos']['srcUrl']#获取json中的链接，类似xpath
systemTime = dic['systemTime']
srcurl = srcurl.replace(systemTime,f'cont-{contID}')
with open("video/"+contID+".mp4","wb") as movie_download:
    movie_download.write(requests.get(srcurl).content)
print("okk")
#替换