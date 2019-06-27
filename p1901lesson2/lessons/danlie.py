class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

a = Singleton(18, 'aaa')
b = Singleton(20, 'bbb')
print(a is b, id(a), id(b))


l = [1, 2, 3]
l = [x+2 for x in l]
print(l)

dic = {'name': 'zs'}
new_dic = {}
for key, val in dic.items():
    new_dic[val] = key
print(new_dic)

new_dic1 = dict(zip(dic.values(), dic.keys()))
print(new_dic1)

new_dic2 = dict([val, key]for key,val in dic.items())
print(new_dic2)

new_dic3 = {v: k for k, v in dic.items()}
print(new_dic3)