import hashlib,hmac
#hashlib支持md5和sha

#md5单向加密
x = hashlib.md5() #生成一个md5对象
x.update("abc".encode("utf-8"))#将"abc"转化成二进制
print(x.hexdigest())

#sha加密
h1 = hashlib.sha1("abc".encode("utf-8"))
print(h1.hexdigest())

h2 = hashlib.sha256("abc".encode("utf-8"))
print(h2.hexdigest())

