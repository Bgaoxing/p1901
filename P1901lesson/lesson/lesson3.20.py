from  dis import dis #将python语言转换为字节码

def plus(a):
    a += 1
    a = a * 100
    return  a
dis(plus)