def say_hello(name,age,city="北京"):
    print(f"大家好，我是{name}，今年{age}岁，来自{city}")

say_hello("Jack",19)  #缺省值

say_hello("Jack",19,"南京")  #主动传参，按顺序

say_hello(age=10,name="Mini",city="邯郸")  #赋值传参，可不按照顺序（如果首参数写了赋值，后面都必须赋值）