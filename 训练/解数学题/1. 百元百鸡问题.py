#题目：公鸡5元1只，母鸡3元1只，小鸡1元3只。求如何用100元买100只鸡。
for x in range(1,21):
    for y in range(1,34):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print(x,y,z)