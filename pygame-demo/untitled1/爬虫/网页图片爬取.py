
import requests,os
root = "D:/python3/PycharmProjects/untitled1/爬虫/爬虫的数据/"
url = "http://scimg.158pic.com/allimg/150403/10-1504031H411E6.jpg"
path = root + url.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")



