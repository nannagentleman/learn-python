# -*- coding: utf-8 -*-
"""
假设某班学生考试，分别输入姓名和分数（姓名不重名），要求输出结果：
a)         分数排行榜，从高到低：姓名  分数
"""
def input_ns():
    names = []
    scores = []
    while 1:
        print "input names and scores, 'q'-exit"
        name = raw_input("please input name:")
        if name in names:
            print name," has been inputed, please change another."
            continue
        elif name == 'q':
            print "You have exited"
            break
        else:
            names.append(name)
        print "input score of ",name
        score = raw_input("score:")
        while 1:
            if not score.isdigit():
                score = raw_input("input again:")
            else:
                scores.append(int(score))
                break
        
    dic = dict(zip(names, scores))
    return dic


def ranked(di):
    d = sorted(di.iteritems(), key = lambda d:d[1], reverse = True)
    return d


print ranked(input_ns())
