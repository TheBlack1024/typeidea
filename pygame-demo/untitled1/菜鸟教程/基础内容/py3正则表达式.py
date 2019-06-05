
# re.match()使用
import re
print(re.match("www","www.runoob.com").span())  # 在起始位置匹配
print(re.match("com","www.runoob.com"))         # 不在起始位置匹配

print("-"*100)

# .*的使用
import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("No match!!")

print("-"*100)

# re.search()使用
import re

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))  # 不在起始位置匹配

print("-"*100)
import re

line = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("Nothing found!!")