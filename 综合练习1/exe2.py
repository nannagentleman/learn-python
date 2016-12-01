# -*- coding: utf-8 -*-
"""
以下是有关BMI的信息：
BMI值計算公式: BMI = 體重(公斤) / 身高2(米2)，
BMI < 18.5：体重过轻；18.5<=BMI<24：正常范围；24≦BMI＜27；
輕度肥胖：27≦BMI＜30；中度肥胖：30≦BMI＜35；重度肥胖：BMI≧35
请根据上述信息，编写程序，并用来判断某人体重情况
"""

def BMI(weight, height):
    bmi = float(weight)/float(height)**2
    return bmi
    
def judge_bmi(bmi):
    if bmi < 18.5:
        return "体重过轻"
    if bmi < 24 and bmi >= 18.5:
        return "正常范围"
    if bmi < 27 and bmi >= 24:
        return "轻度肥胖"
    if bmi < 30 and bmi >= 27:
        return "中度肥胖"
    if bmi <35 and bmi >= 30:
        return "重度肥胖"
        
print judge_bmi(BMI(72, 1.83))