# 场景
# 商店即将期满，现对商品进行统计录入计算机
# 录入商品（商品编号，名称，单价，数量）；
# （根据单价、数量计算该商品能卖出的总价钱，总价钱跟随单价、数量的修改进行动态改变；重复录入当做数量增加的操作）
# 卖出商品（根据商品编号进行售卖）,卖出商品不得超过库存数量
# 修改商品单价
# 查看当前库中所有商品

class Goods:
    def __init__(self, code, name, price, number):
        self.code = code
        self.name = name
        self.price = price
        self.number = number

    @property
    def total(self):
        return int(self.price) * int(self.number)

    def __str__(self):
        return '编号:{}, 名称:{}, 单价:{}, 数量:{}, 总价:{}'\
            .format(self.code, self.name, self.price, self.number, self.total)


class Operator:
    goodslist = []

    def addgoods(self):
        code = input('输入商品编号:')
        name = input('输入商品名称:')
        price = input('输入商品单价:')
        number = input('输入商品数量:')

        # 形成一个商品
        goods = [code, name, price, number]
        # 加入到商品列表下
        self.goodslist.append(goods)


    def sellgoods(self):
        code = input('请输入商品编号：')
        n = int(input('请输入购买数量：'))
        for good in self.goodslist:
            if good[0] == code and n < int(good[3]):
                n -= int(good[3])
                print('售出成功')
                break
            print('商品不存在，请重新选择')

    def change(self):
        code = input('请输入商品编号：')
        for good in self.goodslist:
            if good[0] == code:
                newprice = input('请输入新价格:')
                good[2] = newprice
                print('修改成功')
                break
            print('商品不存在，请确认')

    def startinput(self):
        while True:
            print('1、录入商品')
            print('2、卖出商品')
            print('3、修改商品单价')
            print('4、查看当前库中所有商品')
            print('5、退出')
            n = int(input('请选择:'))
            if n == 1:
                self.addgoods()
            elif n == 2:
                self.sellgoods()
            elif n == 3:
                self.change()
            elif n == 4:
                for good in self.goodslist:
                    print(good)
            elif n == 5:
                break
            print('录入结束')


if __name__ == '__main__':
    kobe = Operator()
    kobe.startinput()