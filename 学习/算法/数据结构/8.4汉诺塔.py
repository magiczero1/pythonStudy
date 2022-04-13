def moveTower(height,fromPole,withPole,toPole):
    if height > 0 :
        moveTower(height-1,fromPole,toPole,withPole)    #将上面n-1个先移动至2号柱
        moveDisk(height,fromPole,toPole)    #将底下一个移动至3号柱
        moveTower(height-1,withPole,fromPole,toPole)    #将2号柱的盘子重新移回1号柱

def moveDisk(disk,fromPole,toPole):
    print(f"将盘片{disk}从{fromPole}移动到{toPole}")

print(moveTower(4,"A","B","C"))
