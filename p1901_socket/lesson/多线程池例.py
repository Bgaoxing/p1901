# 原始题
# import time
# def say(name_list):
#     print('hello', name_list)
#     time.sleep(2)
# name_list = ['kobe', 'cuter', 'iv', 'tmc']
# start_time = time.time()
# for i in range(len(name_list)):
#     say(name_list[i])
# print('{}秒'.format(time.time() - start_time))


# 改用多线程池(有错误，待修改)
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def say(name_list):
    print("Hello ", name_list)
    time.sleep(2)

name_list = ['kobe', 'cuter', 'iv', 'tmc']
start_time = time.time()
pool = ThreadPoolExecutor(20)
function_list = [name_list]
pool_list = list()
for i in function_list:
    pool_list.append(pool.submit(i))
for i in as_completed(pool_list):
    say(name_list)
print('{}秒'.format(time.time() - start_time))