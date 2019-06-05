
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob

a = glob.glob('*.py')
b = 0
for i in a :
    b += 1
    print(b,"--",i)

print("="*100)

# 命令行参数
import sys
print(sys.argv)

print("="*100)

# 时间与日期
from datetime import date
now = date.today()
print(now)
t = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(t)

# 计算年龄
birthday = date(1994, 10, 21)
age = now - birthday
a = age.days
print(a)