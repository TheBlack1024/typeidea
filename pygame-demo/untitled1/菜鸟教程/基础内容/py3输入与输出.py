

# 输出格式美化

a ,b= "tanheming",12345
print(str(a),str(b)) # 用户易读形式
print(repr(a),repr(b)) # 解释器易读形式
print(a,b)

print(str(1/7))
print(1/7)

h = "tanheming\n"
print(h)
print(repr(h))# repr函数可转义特殊字符

print("姓名是%s!ID是%s!"%(a,b))
print("姓名是{0}！ID是{1:10d}！".format(a,b))
print("姓名是{0}！ID是{1:5f}！".format(a,b))

print("="*100)








