# -*- coding: utf-8 -*-
"""
将如下内容存储到一个文本文件中
And since they did not see fit to acknowledge God, God gave them up to a debased mind and things that should no be done. They were filled with every kind of wickedness, evil, covetousness, malice. Full of envy, murder, strife, deceit, craftiness, they are gossips, slanderers, God-haters, insolent, haughty, boastful, inventors of evil, rebellious toward parents, foolish,faithless, heartless, ruthless. They know God's decree, that those who practice such things deserve to die--yet they not only do them but even applaud others who practice them. (ROMANS 1:28-32)
要求，在英文句号处换行。
"""

def f(text):
    text = text.replace('.', '.\n')
    return text

t = "And since they did not see fit to acknowledge God, God gave them up to a debased mind and things that should no be done. They were filled with every kind of wickedness, evil, covetousness, malice. Full of envy, murder, strife, deceit, craftiness, they are gossips, slanderers, God-haters, insolent, haughty, boastful, inventors of evil, rebellious toward parents, foolish,faithless, heartless, ruthless. They know God's decree, that those who practice such things deserve to die--yet they not only do them but even applaud others who practice them. (ROMANS 1:28-32)"

with open("1.txt", "w") as n:
    n.write(f(t))
