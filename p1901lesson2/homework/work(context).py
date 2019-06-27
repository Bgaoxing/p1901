# class Foo(object):
#     def __init__(self):
#         print('实例化一个对象')
#     def __enter__(self):
#         print('进入')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('退出')
#
# obj = Foo()
#
# with obj:
#     print('正在执行')

class Foo(object):

    def __init__(self):
        print('实例化一个对象')

    def __enter__(self):
        print('进入')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出')
        return True

obj = Foo()

# 出现异常时，如果 __exit__ 返回 False（默认不写返回值时，即为False），则会重新抛出异常，
# 让with 之外的语句逻辑来处理异常，这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理
with obj:   # with 上下文管理器：
                     #  语句体
    raise ImportError
    print('正在执行')