
# 变量交换

# 临时变量法
x,y = "LOVE",2

t = x
x = y
y = t
print(x,y)

# 多变量赋值法
x,y = "tanheming",4

x,y = y,x
print(x,y)

# 异域法--只是数据型不然会报错
a,b = 5,6

a = a^b
b = a^b
a = a^b
print(a,b)

print("="*100)

# 优化增加输入字符的判断以及异常输出
while True:
    try:
        num=float(input('请输入一个数字：'))
        if num==0:
            print('输入的数字是零')
        elif num>0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字')

print("="*100)

# Python 打印阿姆斯特朗数
for i in range(1000):
    temp = i
    n = len(str(i))
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if i == sum:
        print(i,end=" ")
print()
print("="*100)
# 引入日历模块
import calendar

# 输入指定年月
#yy = int(input("输入年份: "))
#mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(2019, 3))

print("="*100)

# 递归函数使用示例
def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))


# 获取用户输入
nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_fibo(i))

print("="*100)
# 引入 datetime 模块
import datetime

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# 输出
print(getYesterday())