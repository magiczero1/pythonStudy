#功能表
#①添加：序号(自动生成)、姓名、手机号、QQ号
#②修改：姓名、手机号、QQ号  需要输入序号
#③删除：删除单个信息
#④显示所有名片
#⑤查询名片
#⑥退出系统


def first_page():
    print("名片管理系统1.0".center(20))
    print('''1.添加名片
2.修改名片
3.删除名片
4.显示所有名片
5.查询名片
6.退出系统''')
    print("-"*20)

person_list = []

def add_person(index,name,tel,QQ):
    person_message = {"序号": index, "姓名：": name, "手机号": tel, "QQ号": QQ}
    person_list.append(person_message)
    return person_list

def person_index(i):
    if i == 0:
        return 0
    else:
        return i+1

def funcs():
    first_page()
    func_n = input("请选择功能:")
    index = person_index()
    if func_n in ["1",1]:
        name = input("请输入姓名：")
        tel = input("请输入手机号：")
        QQ = input("请输入QQ号：")
        add_person(index,name,tel,QQ)
        index += 1

    if func_n in ["4", 4]:
        print(person_list)

funcs()



