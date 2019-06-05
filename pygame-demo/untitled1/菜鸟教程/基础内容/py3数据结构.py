
# 遍历字典技巧
# items()同时释放键值

a = {1:"tan",2:"he",3:"ming"}
for k,v in a.items():
    print(k,v)

# enumerate()函数获取索引位置和值

for x, y in enumerate(["tan","he","ming"]):
    print(x,y)

# zip()同时遍历两个或更多序列

t = ["1","2","3","4","5"]
b = ["a","b","c","d","e"]

print("="*100)
for q,p in zip(t,b):
    print(q,p)
    print("我是%s！你是%s！" %(q, p),end="")
    print("我是{0}！你是{1}！".format(q,p))



