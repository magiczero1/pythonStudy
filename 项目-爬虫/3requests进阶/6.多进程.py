from multiprocessing import Process
def func():
    for i in range(1000):
        print("创建子进程")
if __name__ == '__main__':
    p = Process(target=func)
    p.start()