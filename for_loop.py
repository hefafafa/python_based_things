"""<-----------------for的简单循环------------------->"""

import random


name = "超级他吗 可爱合法法"

for x in name:
    print (x)

"""<-----------------for的遍历查询待处理数据集里有几个对应字母------------------->"""
wait = "abcadaksjhfwekgjwfkjasfa;klfhkhbbcakb"
i = 0

for x in wait:
    if x == "a":
     i += 1

print (i)    
"""<-----------------通过range来将数字变为序列------------------->"""
for x in range(49):
    print(x)

for x in range(1,49):
    print(x)

range(1,49,4)
for x in range(1,49,4):
    print(x)

"""<-----------------通过for建立乘法表------------------->"""
for i in range(1,10):
    print()
    for x in range(1,i+1):
        print(f"{x}x{i}={i * x}\t", end='')

"""<-----------------控制循环中断------------------>"""
for i in range(1,6):
    print(f"第{i}次")
    continue
    print("附加")

for i in range(1,6):
    print(f"第{i}次")
    break
    print("附加")

#for countinue 是跳过本次循环之后进入下一次循环， break是直接截断这个循环并执行循环外的语句
"""<-----------------用for循环来发工资------------------>"""
money = 10000

for i in range(1,21):
    score = random.randint(1,10)

    if score < 5:
        print(f"第{i}个员工没有工资")
    elif money < 1000:
        print(f"公司没钱了")
        break
    else: 
        money -= 1000
        print(f"给第{i}个员工发了工资, 工资还剩下{money}")