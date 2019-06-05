
if 0:
    import requests # 引入requests模块
    url = "http://www.qq.com"
    vk = {"User-Agent":"Mozilla/5.0"}
    r = requests.get(url,headers = vk) # 获取网页内容,伪装“User-Agent”
    data = r.content
    #b = requests.get("http://www.qq.com")
    print(r.status_code)

    r.encoding = "utf-8"
    # print(r.text)

    print(type(r))
    print(r.headers)
    print(r.request.headers)
    print(r.encoding)
    print(r.apparent_encoding)

    print("="*100)

    #print(b.status_code)
    #print(b.headers)
    #print(b.encoding)
    #print(b.apparent_encoding)
    #print(b.text)

    with open("tenxun.txt","wb") as f:
        f.write(data)

    with open("tenxun.txt","r") as f:
        b = f.read()
        print(b)
else:
    pass

if 0:
    from bs4 import BeautifulSoup
    import bs4
    import requests
    url = "http://www.gaokaopai.com/paihang.html"
    r = requests.get(url,timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "htmlcss.parser")
    for tr in soup.find("table").children:
        if isinstance(tr, bs4.element.Tag):
            if tr("td")==[]:
                continue
            else:
                tds = tr("td")
                for td in tr.children:
                    if isinstance(td, bs4.element.Tag):
                        if td("a")==[]:
                            continue
                        else:
                            tas = td("a")
                            if tas[0].string==None:
                                continue
                            else:
                                print(tds[0].string,tas[0].string,tds[2].string)
                #ulist.append([tds[0].string, tds[1].string, tds[3].string])
                #print(soup.prettify())

if 0:
    import requests
    url = "https://s.taobao.com/search?q=书包"
    vk = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url,params=vk, timeout=30,)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)

if 0:
    # CrawBaiduStocksA.py
    import requests
    from bs4 import BeautifulSoup
    import traceback
    import re


    def getHTMLText(url):
        try:
            r = requests.get(url,timeout = 30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""


    def getStockList(lst, stockURL):
        html = getHTMLText(stockURL)
        soup = BeautifulSoup(html, "htmlcss.parser")
        a = soup.find_all("a")
        for i in a:
            try:
                href = i.attrs["href"]
                lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
            except:
                continue

    def getStockInfo(lst, stockURL, fpath):
        for stock in lst:
            url = stockURL + stock + ".htmlcss"
            html = getHTMLText(url)
            try:
                if html == "":
                    continue
                infoDict = {}
                soup = BeautifulSoup(html, "htmlcss.parser")
                stockInfo = soup.find('div', attrs={"class": "stock-bets"})

                name = stockInfo.find_all(attrs={"class": "bets-name"})[0]
                infoDict.update({"股票名称": name.text.split()[0]})

                keyList = stockInfo.find_all("dt")
                valueList = stockInfo.find_all("dd")
                for i in range(len(keyList)):
                    key = keyList[i].text
                    val = valueList[i].text
                    infoDict[key] = val

                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(str(infoDict) + "\n")
            except:
                traceback.print_exc()
                continue


    def main():
        stock_list_url = "http://quote.eastmoney.com/stocklist.html"
        stock_info_url = "https://gupiao.baidu.com/stock/"
        output_file = "D:/python3/PycharmProjects/untitled1/爬虫/爬虫的数据/BD股票.txt"
        slist = []
        getStockList(slist, stock_list_url)
        getStockInfo(slist, stock_info_url, output_file)


    main()

