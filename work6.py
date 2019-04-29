ee = 'afjghdfraaaasdenas'
cc='11222333'
def max_letter_count(n):
  list4 = []
  list1 = []
  list2 = []
  for i in n:
    list3 = []
    count_max = n.count(i)
    list3.append(i)
    list3.append(count_max)
    list1.append(list3)
    list2.append(count_max)
  num=max(list2)
  for i in range(len(list2)):
    if list2[i] == num:
      list4.append(list1[i][0])
  return list(set(list4)),'字符出现最大次数为:%d' % num
print(max_letter_count(ee))


key = 13;
c =  [2,3,5,7,11,13,17,19,23,29,31, 37, 41,43,47];
lo, hi= 0,len(c)-1
def BinarySearch(key,c):
    lo, hi= 0,len(c)-1
    while lo<=hi:
        mid = int(lo+(hi-lo)/2)
    if key<c[mid]:
        hi = mid-1
    elif key>c[mid]:
        lo = mid+1
    else:
        return print("{}在数组中的索引为{}".format(key, mid))
    return print("{}不在该数组中".format(key))
BinarySearch(key,c)



class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

class Solution1:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        a=1;b=2;c=3
        for i in range(3,n+1):
            c=a+b;a=b;b=c
        return c
