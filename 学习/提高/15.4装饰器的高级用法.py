#功能背景：在不修改playGame原函数的基础上，增加时间限制器。
#①不能报错   ②能对时间进行限制，晚于22点不允许玩游戏
def timeLimit(fn):

    def Time(name,game,*args,**kwargs):
        t = kwargs.get("clock",20)
        if t < 22:
            fn(name,game)
        else:
            print("太晚了，赶紧睡觉去")
    return Time

@timeLimit
def playGame(name,game):
    print(f"{name}正在玩《{game}》")

playGame("张三","法外狂徒",30)
playGame("张三","法外狂徒",clock=30)