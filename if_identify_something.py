import random
"""<-----------------下边是Boolean------------------->"""
真 = True
假 = False
print(f"真的变量内容为{真},变量类型为{type(真)}")
print(f"真的变量内容为{假},变量类型为{type(假)}")

真假 = 真 == 假
print(f"判断真假为 {真假}")

"""<-----------------下边是if判断------------------->"""

"""年龄 = input("你多少岁了")
if 年龄 >= 18:
    print("那么你成年了")"""

# ↑此条例并不成立，因为年龄是str类型，需要手动修改类型

年龄 = input("你多少岁了")
if int(年龄) >= 18:
    print("那么你成年了")
#或者
年龄 = int(input("你多少岁了"))
if 年龄 >= 18:
    print("那么你成年了")
else:
    print("那么你没有成年")

"""<-----------------下边是if_else的组合判断------------------->"""

身高 = int(input("输入你的身高"))
if 身高 >= 180:
    print ("你好高啊？")
elif 身高 <= 90:
    print ("你是小孩吧")
else: 
    print("okok")

# 快速注释的方法为选中多行
# 然后摁ctrl加/就可以添加注释
# 同样再次选中后重复操作可以解除注释

"""<-----------------下边是if_else的嵌套判断------------------->"""

num = random.randint(1,10)
guess = int(input("你猜的数字"))
if guess == num:
    print("猜对了")
else:
    if guess > num:
        print("猜大了")
    else:
        print("猜小了")

    guess = int(input("你猜的数字"))

    if guess == num:
        print ("猜对了")
    else:
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")

        guess = int(input("你猜的数字"))

        if guess == num:
            print ("猜对了")
        else:
            if guess > num:
                print("猜大了")
            else:
                print("猜小了")

        print("你没有机会猜了")