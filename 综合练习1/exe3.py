# -*- coding: utf-8 -*-
"""
某商品的销售。该商品具有：
a)         零售价
b)         商品成本
c)         销售数量
d)         批发折扣百分比
e)         批发起始数量
每次商品销售后，要计算出该商品：
f)          总销售额：对于大于批发起始数量的部分按照批发价格计算
g)         总利润
（以上所有涉及到金额部分准确到小数点后两位，即分，如2.34元）
"""

class product(object):
    def __init__(self, price, cost, percent, min_num):
        self.price = price
        self.cost = cost
        self.percent = percent
        self.min_num = min_num
  
    def total_return(self, num):
        if num > self.min_num:
            p = self.price*num*self.percent
            return '%.2f' %p
        else:
            p = self.price * num  #是否需要加self ？
            return '%.2f' %p
            
def total_earning(obj, num):
    if num > obj.min_num:
        e = obj.price * num * obj.percent - obj.cost*num
        return '%.2f'% e
    else:
        e = (obj.price-obj.cost) * num 
        return '%.2f'% e
        
if __name__ == "__main__":
    p = product(25, 10, 0.5, 1000)
    print total_earning(p, 1000)
    print p.total_return(1000)   #这两种方法都可以吗？
