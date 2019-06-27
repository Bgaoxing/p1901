# 查看字节码
import dis
num = 0
def add():
    global num
    num += 1

print(dis.dis(add))

# 字节码
# 源代码