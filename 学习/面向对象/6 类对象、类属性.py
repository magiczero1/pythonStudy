class Plants():
    type = "植物"#类属性,只能通过类对象进行更改

    def __init__(self,name,hp,mp,star):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.star = "⭐️"*star

    def attack(self):
        atk = self.hp*0.8

    def __str__(self):
        return f"【英雄名：{self.name}】;【星级:{self.star}】;【生命值：{self.hp}  法力值：{self.mp}】".replace(";","\n")


print(Plants.type)

chilly = Plants("火爆辣椒🌶",1500,100,3)
pumpkin= Plants("贫嘴南瓜🎃",1200,90,2)
onion = Plants("感人洋葱🧅",900,180,3)


print(chilly.type)#可以通过实例对象查看类属性
chilly.type = "动物"#此时实例对象为自己添加了新的属性，并没有更改类属性。
print(chilly.type)
print(Plants.type)

print(chilly)
print()
print(pumpkin)
print()
print(onion)