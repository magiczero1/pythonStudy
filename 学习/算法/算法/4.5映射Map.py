class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size     #初始化key空间
        self.data = [None] * self.size    #初始化value空间

    def hashfunction(self,key):   #设计哈希函数
        return key%self.size

    def rehash(self,oldhash):    #处理具有倍数关系的哈希值
        return (oldhash+1)%self.size

    '''插入'''
    def put(self,key,data):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] == None:       #如果该hash是None，则更新key-value对
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:                                   #否则重新判断
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data     #更新key-value对
            else: #若该key下存在value，即散列冲突
                nextslot = self.rehash(hashvalue)   #查找下一个hash块
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot) #递归调用

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    '''获取'''
    def get(self,key):
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] !=None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

    '''特殊方法实现[]访问'''
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        return self.put(key,data)
