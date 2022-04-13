def add(a,b):
    '''
    求和函数
    :param a:第一个数字
    :param b:第二个数字
    :return: 两个数字相加
    '''
    return a+b

#利用help查看函数的说明
help(add)  #不要加()


#python中参数类型的建议，仅能提供建议
def mutiple(a:int,b:int):
    '''
    求积函数
    :param a: 数字1
    :param b: 数字2
    :return:  积
    '''
    return a*b