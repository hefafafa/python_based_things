# 这里是注释，一半用空格来隔开
"""三个引号里就是多行注释
也就是一大段

"""
print("Hello World!")

"""<-----------------下边是变量------------------->"""
MyMoney = 100
print("我的钱是:", MyMoney, "块钱")
coin = 5
coins = MyMoney / coin
print("那么我有", coins,  "的硬币")
MyMoney = MyMoney - 3 * coin
coins = MyMoney / coin
print("我要买一个价值3xcoin的东西，那么我还剩下", coins,  "的硬币，也就是", MyMoney, "块钱")

"""<-----------------下边是检查类型------------------->"""
print(type(MyMoney))
print(type(coins))

MyMoney_type = type(MyMoney)
print(MyMoney_type)
print(type(MyMoney_type))

"""<-----------------下边是变换变量------------------>"""
Str_MyMoney = str(MyMoney)
print(Str_MyMoney)
print(type(Str_MyMoney))

NewFloat1 = 11.49999
NewFloat2 = 11.50000
NewFloat3 = 11.50001

print(int(NewFloat1), int(NewFloat2), int(NewFloat3))
#所以关于转换字符时候，float会直接去掉小数点后的数字而不是进位或者向上取整

"""<-----------------下边是标识符测试------------------>"""
可乐 = 3
鱼丸 = 5

可乐和鱼丸 = 可乐 + 鱼丸
print(可乐和鱼丸)

"""<-----------------下边是运算符测试------------------>"""

#已有的东西: MyMoney = 85，coin = 5， coins = 17.0，可乐 = 3， 鱼丸 = 5， 可乐和鱼丸 = 8

print(MyMoney - 可乐)
print(可乐和鱼丸 + 可乐)
print(可乐 * 5)
print(coin / 鱼丸)
print(coin / 可乐 , coin // 可乐, coin % 可乐)
print(MyMoney - 可乐和鱼丸 ** 3)

"""<-----------------下边是定义字符测试------------------>"""

我的名字 = '合法法'
我的年龄 = 21
我的取向 = "正常"
我的简介 = """这里是简介，
然后可以换行， 这个简介必须要同行并且跟在等号后边
因为是三个双引号，不在一条线上就会被认定为注释 """

bottle1 = "农夫山泉'长白山的'水"
bottle2 = '元气森林"很贵"'
bottle3 = """ 旺仔牛奶 "有点甜不说 '还挺好喝呢'" """
bottle4 = '\'这他吗是杀虫剂'
# \是转义字符，可以让后边跟着的一个引号不算为引号
print(bottle1, bottle2, bottle3)
print(bottle4)
水瓶组合 = "这堆水是%s和%s的组合" % (bottle3, bottle1)
print(水瓶组合)

水瓶组合 = "这堆水是%a和%s的组合" % (bottle3, bottle1)
print(水瓶组合)

水瓶组合 = "这堆水是%e和%s的组合" % (MyMoney, bottle1)
print(水瓶组合)
水瓶组合 = "这堆水是%e和%s的组合" % (可乐, bottle1)
print(水瓶组合)
水瓶组合 = "这堆水是%r和%s的组合" % (bottle3, bottle1)
print(水瓶组合)
水瓶组合 = "这堆水是%r和%s的组合" % (可乐, bottle1)
print(水瓶组合)
水瓶组合 = "这堆水是%u和%s的组合" % (可乐, bottle1)
print(水瓶组合)
# %s 变换并添加string类型, %d 变换并添加int类型， %f 变换并添加float类型
"""<-----------------下边是更加快速占位测试------------------>"""
print(f"我叫{我的名字}， 年龄是{我的年龄}, 我现在有{MyMoney}的钱，还有{NewFloat3}")
print(f"我叫{我的名字}， 年龄是{我的年龄}, 我现在有{MyMoney}的钱，还有{可乐 * 鱼丸}")

"""<-----------------下边是控制精度------------------>"""



# %m.n类型,这里精确后的数字会有四舍五入的规则
a = 123
b = 134.247
print("a的精度%3d" % a)
print("a的精度%5d" % a)
print("a的精度%3.7d" % a)
print("a的精度%.7d" % a)
print("a的精度%5.7d" % a)

print("b的精度%3d" % b)
print("b的精度%5d" % b)
print("b的精度%3.3d" % b)
print("b的精度%5.3d" % b)
print("b的精度%5.7d" % b)
print("b的精度%.7d" % b)

print("b的精度%3f" % b)
print("b的精度%5f" % b)
print("b的精度%3.3f" % b, "你好")
print("b的精度%5.3f" % b, "你好")
print("b的精度%5.7f" % b, "你好")
print("b的精度%.7f" % b)
print("b的精度%.5f" % b)