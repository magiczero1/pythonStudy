from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def func(name):
    for i in range(100):
        print(name)
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as T:      #创建线程池
        for i in range(100):
            T.submit(func,name=f"线程{i}")
    print("ok")