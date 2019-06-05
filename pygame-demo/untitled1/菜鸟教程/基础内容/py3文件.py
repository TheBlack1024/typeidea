# 文件尝试1
f = open("TXT.txt","w")
f.write("tanheming\n")
f.close()

# 文件尝试2
f = open("TXT.txt","r")
book = f.read()
print(book)
f.close()

# 文件尝试3
f = open("TXT.txt","a")
f.write("世界之大，我欲游\n")
f.close()

# 文件尝试4
f = open("TXT.txt","r+")
book = f.read()
print(book)
print("-"*100)
f.write("游天下，方知吾之小亦！\n")
book1 = f.read()# 光标在结尾
print(book1)# 打印结果为无
f.close()

print("-"*100)
# 文件尝试5
f = open("TXT.txt","a+")
book = f.read()
print(book)

print("="*100)

# f.readline()读行
f = open("TXT.txt","r")
book = f.readline()
print(book)
book1 = f.read()
print(book1)
f.close()

# f.readlines()读行
f = open("TXT.txt","r")
book = f.readlines()
print(book)
f.close()

print("-"*100)
# 打开一个文件
f = open("TXT.txt", "r")
for line in f:
    print(line, end='')
# 关闭打开的文件
f.close()

with open("TXT.txt", "a+") as f:
    f.write("test.txt")

f = open("TXT.txt","r")