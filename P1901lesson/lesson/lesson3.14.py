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
    def sumprice(self):
        return int(self.price) * int(self.number)

    def __str__(self):
        return '编号:{}, 名称:{}, 单价:{}, 数量:{}, 总价:{}'\
            .format(self.code, self.name, self.price, self.number, self.sumprice)

class Person:
    def __init__(self, name):
        self.name = name

    def showinput(self):
        return int(input('请选择菜单:'))

    def p_addgoods(self, computer):
        code = input('输入商品编号:')
        goods = computer.findgoods(code)
        if goods is not None:
            number = int(input('输入商品数量:'))
            return goods, number
        else:
            name = input('输入商品名称:')
            price = input('输入商品单价:')
            number = int(input('输入商品数量:'))
            newgoods = Goods(code, name, price, number)
            return newgoods


    def p_sellgoods(self, computer):
        code = input('输入商品编号:')
        goods = computer.findgoods(code)
        if goods is not None:
            number = int(input('输入商品数量:'))
            return goods, number

    def p_changegoods(self, computer):
        code = input('输入商品编号:')
        goods = computer.findgoods(code)
        if goods is not None:
            price = input('输入新的单价:')
            return goods, price

class Computer:
    goodslist = []
    def __init__(self):
        self.seller = None


    def shown(self):
        print('1、添加商品')
        print('2、卖出商品')
        print('3、修改商品单价')
        print('4、查看库存')
        print('5、退出')
        n = self.seller.showinput()
        return n

    def addgoods(self):
        result = self.seller.p_addgoods(self)
        if isinstance(result, Goods):
            self.goodslist.append(result)
            print('添加成功')
        else:
            goods = result[0]
            number = result[-1]
            goods.number = goods.number + number
            print('数量添加成功')


    def reducegoods(self):
        result = self.seller.p_sellgoods(self)
        if result is not None:
            goods = result[0]
            number = result[-1]
            if goods.number < number:
                print('当前库存为:{}, 卖完了'.format(goods.number))
                goods.number = 0
            else:
                goods.number = goods.number - number
                print('卖出{}, 还剩{}'.format(number, goods.number))
                if goods.number == 0:
                    print('商品卖完了')


    def changegoods(self):
        result = self.seller.p_changegoods(self)
        if result is not None:
            goods = result[0]
            price = result[-1]
            goods.price = price
            print('单价修改成功，新的商品单价为{}'.format(goods.price))


    def findgoods(self, code):

        for goods in self.goodslist:
            if goods.code == code:
                return goods
            print('商品不存在')

    def boot(self, seller):
        self.seller = seller
        while True:
            n = self.shown()
            if n == 1:
                self.addgoods()
            if n == 2:
                self.reducegoods()
            if n == 3:
                self.changegoods()
            if n == 4:
                for goods in self.goodslist:
                    print(goods)
            if n == 5:
                break



if __name__ == '__main__':
    person = Person('张三')
    computer = Computer()
    computer.boot(person)

