import timeit


def list_append():
    # 向一个空列表添加0-10000元素
    lst = []
    for i in range(10001):
        lst.append(i)

def list_insert_tail():
    # 向一个空列表添加0-10000元素
    lst = []
    for i in range(10001):
        lst.insert(-1, i)

def list_insert_head():
    # 向一个空列表添加0-10000元素
    lst = []
    for i in range(10001, -1, -1):
        lst.insert(0, i)

def list_insert_extend():
    # 向一个空列表添加0-10000元素
    lst = []
    for i in range(10001):
        lst.extend([i])




func_list = [list_append, list_insert_tail, list_insert_head, list_insert_extend]
for func in func_list:
    t = timeit.Timer('func()', globals={'func': func})
    time_taken = t.timeit(number=1000)
    print(f"{func.__name__}运行时间: {time_taken:.5f} seconds")
