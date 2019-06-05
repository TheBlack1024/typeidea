
import requests
import re
r = requests.get("http://python123.io/ws/demo.html")
#print(r.text)
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"htmlcss.parser")

print("="*100,"\n","tag标签个属性认识")
if 0:
    print(soup.prettify()) #解析所有代码
    print("-"*50)
    print(soup.title) #获取抬头
    print(soup.a) #获取标签
    print(soup.a.name) #获取标签名字
    print(soup.a.parent.name) #名字父类名字
    print(soup.a.parent.parent.name) #父类的父类名字
    tag = soup.a
    print(tag.attrs) #标签属性
    print(tag.attrs["class"]) #获取“class”对应的值
    print(tag.attrs["href"]) #获取“href”链接属性内容
    print(type(tag.attrs)) #获取标签属性的类型
    print(type(tag)) #获取标签的类型
    print(type(soup.a.string))
    print(soup.p.string)#获取p标签内的字符串
    print(type(soup.p.string))#获取p标签字符串的类型
else:
    pass

print("="*100,"\n","html代码遍历解析")

if 0:
    print(soup.head) #获取head标签
    print(type(soup.head))
    print(soup.head.contents)#获取head标签的子节点
    print(type(soup.head.contents))
    print(soup.body) #body标签
    print(soup.body.contents)#body子节点信息
    print(len(soup.body.contents))
    print(soup.body.contents[1])
else:
    pass

print("="*100,"\n","代码节点下行遍历")

if 0:
    for child in soup.body.contents:
        print(child)
    print("-"*100)
    for child in soup.body.children:
        print(child)
    print("-"*100)
    for child in soup.body.descendants:
        print(child)
else:
    pass

print("="*100,"\n","代码节点上行遍历")

if 0:
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
else:
    pass

print("="*100,"\n","代码节点平行遍历")

if 0:
    for child in soup.body.next_siblings:
        print(child)
    print("-"*100)
    for child in soup.body.previous_siblings:
        print(child)
else:
    pass

#print(soup.prettify()) #解析所有代码
# print(soup.a.prettify())

print("="*100,"\n","代码信息提取")

if 0:
    print(".find_all()方法的使用")
    print(soup.find_all("a"))#获取名为a的标签
    print(soup.find_all(["a","b"]))#获取a、b的标签
    print("-"*50)
    for tag in soup.find_all(True):#获取soup的所有标签
        print(tag.name,end=" ")
    print()
    print("-"*50)
    for tag in soup.find_all(re.compile("b")):#获取名字是b开头的所有标签，正则表达式的使用
        print(tag.name)

    print("-"*50)
    for link in soup.find_all("a"):#获取a标签里href子标签的内容
        print(link.get("href"))

    print("-" * 50)
    print(soup.find_all("p","course"))#获取p标签里含有course的p标签
    print(soup.find_all(id="link1"))#获取标签中id=link1的标签元素
    print(soup.find_all(id=re.compile("link")))#获取soup中id=link开头的标签元素
    print(soup.find_all(string="Basic Python"))#获取soup中字符串"Basic Python"内容
    print(soup.find_all(string=re.compile("Python")))#获取soup中含有“Python“的字符串
    print(soup("p"))#<tag>()等价于<tag>.find_all()，suop()等价于soup.find_all()


else:
    pass



