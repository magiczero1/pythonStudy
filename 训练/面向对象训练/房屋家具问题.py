#房子（House）属性： 户型、总面积、剩余面积和家具名称列表
#新房子没有任何家具
#将家具名称 追加到 家具名称列表 中
#判断家具面积是否超过 剩余面积 ，若超过 则提示不能添加这件家具

#家具（Furniture）属性：名字 占地面积
#席梦思（bed） 占地4平米
#衣柜（chest） 占地2平米
#餐桌（table） 占地1.5平米

#打印房子时，输出户型，总面积、剩余面积、家具名称列表

class Furniture():
    def __init__(self,name,square):
        self.name = name
        self.square = square

class House(Furniture):
    def __init__(self,house_type,total_square,free_square,fur_list = None):
        self.house_type = house_type
        self.total_square = total_square
        if total_square >= free_square:
            self.free_square = free_square
        else:
            print("您家还把公摊写进自己房产证里呢？")
        if fur_list is None:
            self.fur_list = []

    def add_fur(self,furniture):
        if furniture.square > self.free_square:
            print("您家就屁大点，还想买家具呢")
        else:
            self.fur_list.append(furniture.name)
            self.free_square -= furniture.square

    def __str__(self):
        return f"您家总面积：{self.total_square}m²;您家剩余面积：{self.free_square}m²;您家的家具：{self.fur_list}".replace(";","\n")

bed = Furniture("席梦思",40)
chest = Furniture("衣柜",20)
table = Furniture("餐桌",11.5)

house1 = House("三室一厅",100,70)
house1.add_fur(bed)
house1.add_fur(bed)
house1.add_fur(table)
print(house1)