#建立一个汽车类Auto
#包括轮胎个数，汽车颜色，车身重量，速度等属性
#功能： 加速、减速、停车

#定义一个子类，小汽车CarAuto
#增加空调属性，CD属性
#重写加、减速方法

class Auto():
    def __init__(self,wheels,color,weight,speed=100):
        self.wheels = wheels
        self.color = color
        self.weight = weight
        self.speed = speed

    def __str__(self):
        return f"↓车辆属性↓；车轮：{self.wheels}；车身颜色：{self.color}；车重：{self.weight}；最高时速：{self.speed}".replace("；","\n")

    def speed_up(self):
        self.speed = int(self.speed)
        if self.speed<200:
            self.speed += 10
        else:
            self.speed = 200

    def speed_down(self):
        self.speed = int(self.speed)
        if self.speed > 0:
            self.speed -= 10
        else:
            self.speed = 0

    def stop(self):
        self.speed = 0

class CarAuto(Auto):
    def __init__(self,wheels,color,weight,speed,air_condition,CD):
        super(CarAuto, self).__init__(wheels,color,weight,speed)
        self.air_condition = air_condition
        self.CD = CD

    def speed_up(self):
        self.speed = int(self.speed)
        if self.speed < 250:
            self.speed += 15
        else:
            self.speed = 200

    def speed_down(self):
        self.speed = int(self.speed)
        if self.speed > 0:
            self.speed -= 5
        else:
            self.speed = 0

    def __str__(self):
        return f"↓车辆属性↓；车轮：{self.wheels}；车身颜色：{self.color}；车重：{self.weight}；最高时速：{self.speed}；空调：{self.air_condition}；CD功能：{self.CD}".replace("；","\n")


car = Auto(4,"Black","10T",120)
print(car)
print("-"*10)

buick = CarAuto(10,"Rinbow","100T",150,"有","无")
print(buick)
print("-"*10)

car.speed_up()
print(car.speed)