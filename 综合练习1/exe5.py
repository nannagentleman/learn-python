# -*- coding: utf-8 -*-
"""
美国体育作家Bill James发明了一种算法，通过该算法能够知道在NBA比赛中，领先对手多少分是“安全的”，即能够确保最终赢得比赛。他的算法如下：
a)         获取领先一队的分数
b)         减去三分
c)         如果目前领先队控球，那么加上0.5分；如果是落后队控球，减去0.5分（数字小于零则变成零）
d)         计算平方后的结果。
e)         如果结果比当前比赛剩下的时间秒数大，那么这个领先是安全的。
"""

def is_safe(score, kongqiu, time):
    score -= 3
    if kongqiu:
        score += 0.5
    else:
        score -= 0.5
    if score < 0:
        score = 0
    score = score ** 2
    if score > time:
        return True
    else:
        return False
        
print is_safe(23, False, 380)