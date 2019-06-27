class Good:
    def __init__(self, barcode, name, price, count):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.count = count

    @property
    def sumprice(self):
        return self.price * self.count

    def __str__(self):
        return '商品编号:{}, 名称:{}, 单价:{}, 数量:{}, 总价:{}'.format(
            self.barcode,
            self.name,
            self.price,
            self.count,
            self.sumprice
        )


class Person:

    def __init__(self, name):
        self.name = name

    def inputmenu(self):
        return int(input('选择菜单:'))

    def seller_addgood(self, computer):
        """
        1、输入商品编号
        2、将编号传递给计算机查找
        3、将计算机查找结果进行对应操作
          存在：输入商品数量
          不存在：输入详细信息
        4、传递给计算机做对应操作
        :return:
        """
        barcode = input('输入商品编号:')
        good = computer.searchgood(barcode)
        if good is not None:
            count = int(input('输入需要增加的商品数量:'))
            return good, count
        else:
            name = input('输入商品名称:')
            price = int(input('输入新商品的单价:'))
            count = int(input('输入新商品的数量:'))
            newgood = Good(barcode, name, price, count)
            return newgood


    def seller_sellgood(self, computer):
        """
               1、输入商品编号
               2、根据计算机查询结果进行操作
                存在，输入数量
                不存在，不操作
               """
        barcode = input('输入商品编号:')
        good = computer.searchgood(barcode)
        if good is not None:
            count = int(input('输入需要出售的数量:'))
            return good, count

    def seller_editgood(self):
        pass

class Computer:

    goods = []  # 存放商品信息

    def __init__(self):
        self.seller = None

    def showmenu(self):
        print('1、添加商品')
        print('2、卖出商品')
        print('3、修改商品单价')
        print('4、查看库存')
        print('5、退出')
        n = self.seller.inputmenu()
        return n

    def addgood(self):
        """
        1、售货员输入商品编号给计算机
        2、计算机通过编号查找该商品是否存在
        3、将查到结果告诉售货员
        4、如果商品存在，则售货员输入商品数量
          将商品的数量给计算机，计算机进行对应修改
        5、如果商品不存在，则售货员输入商品单价、数量
          将信息给计算机，计算机进行新增
        """
        # 当前self代表computer1
        result = self.seller.seller_addgood(self)

        if isinstance(result, Good):
            self.goods.append(result)
            print('新增成功')
        else:
            good = result[0]
            count = result[-1]
            good.count = good.count + count
            print('数量添加成功')

    def reducegood(self):
        """
                1、售货员输入商品编号
                2、计算机使用编号进行查找
                3、将查找结果给售货员
                4、如果存在，则售货员输入需要减少的数量
                5、如果不存，售货员不能操作
                :return:
                """
        result = self.seller.seller_sellgood(self)
        if result is not None:
            good = result[0]
            count = result[-1]
            if count > good.count:
                print('大于了库存，当前库存:{}, 卖完了'.format(good.count))
                good.count = 0
                # self.goods.remove(good)
            else:
                good.count = good.count - count
                print('卖出{}, 剩余{}'.format(count, good.count))
                if good.count == 0:
                    print('商品卖完了')
                    # self.goods.remove(good)

    def editgood(self):
        pass

    def searchgood(self, barcode):
        for good in self.goods:
            if good.barcode == barcode:
                return good
        print('没找到')

    def showallinfo(self):
        pass

    def poweron(self, seller):
        # 开机之后，该售货员确定
        self.seller = seller

        while True:
            n = self.showmenu()
            if n == 1:
                self.addgood()
            elif n == 2:
                self.reducegood()
            elif n == 3:
                pass
            elif n == 4:
                for good in self.goods:
                    print(good)
            elif n == 5:
                break


if __name__ == '__main__':
    zhangsan = Person('张三')
    computer1 = Computer()
    computer1.poweron(zhangsan)