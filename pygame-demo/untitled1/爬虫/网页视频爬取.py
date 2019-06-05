
import requests,os
root = "D:/python3/PycharmProjects/untitled1/爬虫/爬虫的数据/"
url = "https://domhttp.kksmg.com/2019/03/07/h264_450k_mp4_ce1228f026808d942b076c29ab1536e9_ncm.mp4"
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
