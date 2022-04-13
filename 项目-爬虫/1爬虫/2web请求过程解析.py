#1.服务器渲染：在服务端直接让数据和html进行渲染，如百度等网站
#2.客户端（本地）渲染：（需要抓包）
#   第一次返回一个html骨架
#   第二次返回数据后，进行数据整合。如豆瓣

#请求
'''
请求行-> 请求方式（get/post) 请求url地址、协议
请求头-> 放一些服务器要使用的附加信息
UA：User-Agent请求载体的身份标识
Referer防盗链，用于反反爬
cookie

请求体-> 一般放一些请求参数
'''

#响应
'''
状态行->协议 状态码404、500等
响应头->放一些客户端要使用的一些附加信息

响应体->服务器返回的真正客户端要用的内容(HTML,json)等
'''