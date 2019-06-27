# def func1(method):  # method 代表 func(1, 3, nam='zs')
#     def wrapper(*args, **kwargs):
#         for key, value in kwargs.items():
#             if key == 'name':
#                 raise EOFError
#         return method(*args, **kwargs)
#     return wrapper
#
# @func1
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1, 3, nam='zs')

# class func1:
#     def __init__(self, method):
#         self.method = method
#     def __call__(self, *args, **kwargs):
#         for key, value in kwargs.items():
#             if key == 'name':
#                 raise EOFError
#         return self.method(*args, **kwargs)
#
# @func1
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1, 3, nam='zs')

# def function(kword): # @function(['name', 'gender']) 返回装饰器wrapper
#
#     def wrapper(method): # func
#         def func(*args, **kwargs): # func(1, 3, nam='zs')
#
#             for key in kword:
#                 if key in kwargs.keys():
#                     raise EOFError
#             return method(*args, **kwargs)
#         return func
#     return wrapper
#
# @function(['name', 'gender'])
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# func(1, 3, nam='zs')

def argument_validator(**kwargs_template):
    template = {}
    for k, v in kwargs_template.items():
        arg_name, arg_type = k.split("__")
        arg_required = v
        template[arg_name] = (arg_type, arg_required)

    def method_func(method):
        def wrapper(*args, **kwargs):
            new_kwargs = {}
            new_kwargs.update(kwargs)

            for arg_name, (arg_type, arg_required) in template.items():
                if arg_required and arg_name not in kwargs:
                    raise Exception("Required argument: " + arg_name)
                new_kwargs[arg_name] = eval(arg_type)(kwargs[arg_name])

            return method(*args, **new_kwargs)

        return wrapper

    return method_func

@argument_validator(username__str=1, age__int=1, gender__int=0)
def my_view(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    my_view(username=4, age='7', gender='6')


# def argment(*args,**kwargs):
#     def wrapper(method):
#         def func(*args, **kwargs):
#
#
#             return method(*args, **kwargs)
#         return func
#     return wrapper
#
# @argment('name', 'age')
# def func(*args, **kwargs):
#     print(args, kwargs)
#
# if __name__ == '__main__':
#     func(name = 'zs', age = 10)


def argment(*args,**kwargs):
    def wrapper(method):
        def func(*args, **kwargs):

            return method
        return func
    return wrapper
@argment('name', 'age')
def func(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    func(name='zs', age=19)




