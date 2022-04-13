import uuid
print(uuid.uuid1())  #基于mac、时间戳、随机数随机生成全局唯一id
print(uuid.uuid4())  #通过伪随机数生成唯一id
print(uuid.uuid3(uuid.NAMESPACE_DNS,"abc")) #基于sapcename生成唯一id，固定不变