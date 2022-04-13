def div(a,b):
    try:
        return a/b
    except:#与try优先级一致，次级
        return "出错了"
    else:  #最后
        return a*b
    finally: #优先级最高
        print("铁汁，计算完毕")

print(div("a",0))