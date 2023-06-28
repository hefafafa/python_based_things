"""<-----------------下边是while和计数器循环------------------->"""
count = 1

while count < 10:
    print ("计数器为", count)
    count += 1

"""<-----------------下边是while计算1到100的和------------------->"""
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
    print (f"result的值是{result},计数器为{i - 1}")

"""<-----------------while嵌套和if一样可以查看if------------------->"""

# 输出99乘法表
a = 1

sum = 0

while a <= 9:
    b = 1
    while b <= a:
        sum = a * b
        print (f"{b}x{a}={sum}\t", end='')
        b += 1
    a += 1
    print()
