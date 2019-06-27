class Person:
    def __init__(self, name, phone, money=0):
        self.name = name
        self.phone = phone
        self.money = money

    def __str__(self):
        return '姓名：{} 电话：{} 余额：{}'.format(self.name, self.phone, self.money)


class Salesperson:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def saler_addperson(self, computer):
        phone = input('请输入电话')
        result = computer.searchephone(phone)
        if result is None:
            name = input('请输入姓名：')
            try:
                money = int(input('请输入开卡金额'))
            except ValueError:
                print('金额必须为数字！请重新添加')
            else:
                if money >= 1000:
                    newperson = Person(name, phone, money)
                    return newperson
                else:
                    newperson = Person(name, phone, money)
                    print('录入成功！')
                    return
        else:
            print('该客户已存在不能重复添加！')

    def saler_delvip(self, computer):
        phone = input('请输入需要注销卡片的客户电话：')
        result = computer.searchephone(phone)
        if result is None:
            print('该客户不存在无法注销！')
            return
        return result

    def saler_addmoney(self, computer):
        phone = input('请输入要充值的账号电话：')
        result = computer.searchephone(phone)
        if result is None:
            print('客户不存在无法充值')
            return
        return result

    def saler_showperson(self, computer):
        phone = input('请输入要查询的客户电话：')
        result = computer.searchephone(phone)
        if result is None:
            print('客户不存在！无法查询')
            return
        return result

class Computer:
    persons = {'一类': []}
    saler = Salesperson('1', 'lwy')

    def searchephone(self, phone):
        for per in self.persons['一类']:
            if per.phone == phone:
                return per

    def addperson(self):
        result = self.saler.saler_addperson(self)
        if result is not None:
            self.persons['一类'].append(result)
            print('您已成为一类VIP客户')

    def delvip(self):
        result = self.saler.saler_delvip(self)
        if result is not None:
            self.persons['一类'].remove(result)
            print('已退出一类vip')

    def addmoney(self):
        result = self.saler.saler_addmoney(self)
        if result is not None:
            try:
                newmoney = int(input('请输入需要充值的金额：'))
            except ValueError:
                print('金额必须为数字，请重新操作')
            else:
                if newmoney >= 1000:
                    result.money =result.money + newmoney
                    print('充值成功！您的账户余额为：{}元。'.format(result.money))
                    return
                print('一类VIP不能充值低于1000元！')

    def showperson(self):
        result = self.saler.saler_showperson(self)
        if result is not None:
            print(result)

    def login(self):
        code = input('请输入工号：')
        name = input('请输入姓名：')
        if self.saler.code == code and self.saler.name == name:
            return self.saler

    def showmenu(self):
        print('1、录入客户信息')  # 根据信息如果大于等于1000生成1类卡
        print('2、注销卡片')
        print('3、一类VIP充值')  # 1类卡客户每次最低存款1000元
        print('4、查看客户卡片状态')
        print('5、退出')
        return int(input('请选择：'))

    def start(self):
        saler = self.login()
        if saler is None:
            print('登录失败')
            return
        print('欢迎{}进入系统'.format(saler.name))
        self.saler = saler
        while True:
            n = self.showmenu()
            if n == 1:
                self.addperson()
            elif n == 2:
                self.delvip()
            elif n == 3:
                self.addmoney()
            elif n == 4:
                self.showperson()
            elif n == 5:
                break


if __name__ == '__main__':
    per1 = Person('zangsan', '1331234567', 1000)
    computer1 = Computer()
    computer1.persons['一类'] .append(per1)
    computer1.start()