"""<-----------------function来计算字符长度----------------->"""
import random


str1 = "合法合法合"
串1 = "我叫合法法"
str2 = "あゆむと申します。"
# def 的作用就是 在def后边的东西被定义为了函数
def 检查长度(data):
    # 当然，data是一个变量，你可以更换为任何变量，此变量可以被代表并且只作用于当前函数的区域
    count = 0
    for i in data:
        count +=1
    print(f"字符串是{data}，长度为{count}")

检查长度(str1)
检查长度(串1)
检查长度(str2)
"""<-----------------function的定义----------------->"""
# 可以注意到 def定义出来的函数并没有给它一个属性比如public private 或者protected
# 当然参数是不必要的（就像上边的data，如果你这个函数只是一个操作，那么我只要搞一个 def 操作1 就行了
# 我也可以接受多个函数，就变成了def 操作(a,b,c,x,y,z)
def 查核酸():
    print ("我要查你核酸\n请输入你的名字",)
    name = input("你的名字是:")
    time = random.randint(1,73)
    
    if time < 48:
        print(f"{name},48小时核酸")
    else:
        print(f"{name},非48小时核酸")

查核酸()

"""<-----------------function来加权平均数---------------->"""
num1 = float(input("num1"))
num2 = float(input("num2"))
num3 = float(input("num3"))

def 加权平均数(x,y,z):
    print(f"第一个数是{x},请输入权重:")
    权x = float(input("权x:"))
    print(f"第二个数是{y},请输入权重:")
    权y = float(input("权y:"))
    print(f"第三个数是{z},请输入权重:")
    权z = float(input("权z:"))
    result = (权x*x + 权y*y + 权z*z)/(x + y + z)
    return print(result)

加权平均数(num1,num2,num3)

#当然我也可以嵌套函数

def 输出信息(data):
    print(f"输入的数字为:{data}, 输入权重:")

def 加权平均数2(x,y,z):
    输出信息(x)
    权x = float(input("权x:"))
    输出信息(y)
    权y = float(input("权y:"))
    输出信息(z)
    权z = float(input("权z:"))
    result = (权x*x + 权y*y + 权z*z)/(x + y + z)
    return print(result)

加权平均数2(num1,num2,num3)

#如果设定的函数并没有返回值，那么默认为none，测试type你会看到
# fun1 = None
# 比如 type(fun1()) 会返回你 <class 'NoneType'>
# None 也就说明返回了一个False，可以用在判断语句中
# 我也可以利用这一点来产生一个变量比如 x = None
# 这时候就说明我有一个变量x，但是这个x并没有值，只是存在一个变量x而已

"""<-----------------function对于变量的域和global---------------->"""
x=1
y=2
z=5
v=None

def fun1(a,b,c):
    print(f"a:{a},b:{b},c:{c}")

    global v
    v=13

    return v

fun1(x,y,z)

print(v)

# 如果一个变量被声明为global的话，说明这个变量会在全局都起作用而不只是当前行
