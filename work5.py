
# 第三题
list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
new_list = []

for a in range(len(list1)):
    new_list.append([])

for i in reversed(list1):
    n = 1
    for j in i:
        new_list[n-1].append(j)
        n += 1

for i in new_list:
    print(i)

# 第四题
l1 = [1, 8, 3, 2, 9, 5, 4, 7]
# for i in l1:
#     if l1.count(i) > 1:
#         l1.remove(i)
# print(l1)

print(set(l1))

# 第一题
for i in range(1, 10):
    for x in range(1,i+1):
        print( '%d X %d = %2d' % (i, x, i*x), end  =  '  ' )
    print('  ')

# 第二题
for i in range(1, 5):
    print("")
    y=5-i
    print(' '*y , end="")
    for k  in range(1, 2*i):
        print('*', end="")


s = '*'
for i in range(1, 8, 2):
    print((s*i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s*i).center(7))

for i in range(7):
    for j in range(6 - i):
        print("  ", end="")
    for k in range(i):
        if k == 0 or k == i - 1:
            print("*", end="   ")
        else:
            print(end="    ")

    print()
for i in range(5, 0, -1):
    for j in range(6 - i):
        print("  ", end="")
    for k in range(i):
        if k == 0 or k == i - 1:
            print("*", end="   ")
        else:
            print(end="    ")
    print()



