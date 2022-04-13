#宠物店类 PetShop
#属性：店名、宠物列表

#宠物狗类PetDog    属性：昵称、性别、年龄、品种     方法：叫、拆家、吃饭
#宠物猫类PetCat    属性：昵称、性别、年龄、品种、眼睛颜色   方法：叫、撒娇、吃饭

class PetShop():
    def __init__(self,shopname,petlist = None):
        self.shopname = shopname
        if petlist is None:
            self.petlist = []
        self.petlist = petlist

    def show_pets(self):
        return self.petlist

class PetDog():
    def __init__(self,nickname:str,sex:str,age:int,type:str):
        self.nickname = nickname
        self.sex = sex
        self.age = age
        self.type = type

    @staticmethod
    def bark():
        return "汪汪"

    def eat(self):
        return f"{self.nickname}开始吃骨头咯🦴"

    def demolition(self):
        return f"{self.nickname}要拆了你的家"



class PetCat():
    def __init__(self,nickname,sex,age,type,eyes_color):
        self.nickname = nickname
        self.sex = sex
        self.age = age
        self.type = type
        self.eyes_color = eyes_color

    @staticmethod
    def bark():
        return "喵喵"

    def eat(self):
        return f"{self.nickname}开始鱼🐟咯"

    def coquettish(self):
        return f"主人摸摸{self.nickname}吧"


hasiki = PetDog("二哈","男",5,"哈士奇")
print(hasiki.bark())
print(hasiki.demolition())