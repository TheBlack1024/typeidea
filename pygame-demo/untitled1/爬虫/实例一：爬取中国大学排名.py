# CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("table").children:
        if isinstance(tr, bs4.element.Tag):
            if tr("td") == []:
                continue
            else:
                tds = tr("td")
                for td in tr.children:
                    if isinstance(td, bs4.element.Tag):
                        if td("a") == []:
                            continue
                        else:
                            tas = td("a")
                            if tas[0].string == None:
                                continue
                            else:
                                ulist.append([tds[0].string, tas[0].string, tds[2].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))

def savedata(datalist,num):
    with open("中国大学排名.xls","w") as f:
        f.write("排名"+"\t"+"学校名字"+"\t"+"总分"+"\n")
        for i in range(num):
            w = datalist[i]
            f.write(w[0]+"\t"+w[1]+"\t"+w[2]+"\n")


def main():
    uinfo = []
    url = "http://www.gaokaopai.com/paihang.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs
    savedata(uinfo,20)



main()