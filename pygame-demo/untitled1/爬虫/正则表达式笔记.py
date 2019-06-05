

if 0:#正则表达式函数介绍
    import re
    #re.search()函数，搜索匹配，返回第一个子串
    match = re.search(r"[1-9]\d{5}","BIT 100081")
    if match:
        print(match.group(0))

     #re.match()函数,从开始位置匹配，返回一个
    match = re.match(r"[1-9]\d{5}","BIT 100081")
    if match:
        print(match.group(0))
    match_1 = re.match(r"[1-9]\d{5}","100081 BIT")
    if match_1:
        print(match_1.group(0))

    #re.findall()函数，搜索匹配返回所有适配子串,列表
    findalllist = re.findall(r"[1-9]\d{5}","BIT100081 BUT100045")
    print(findalllist)
    print(findalllist[0])

    #re.split()函数，搜索匹配，分割返回一个列表
    splitlist = re.split(r"[1-9]\d{5}","BIT100081 BUT100045 NTU100035",maxsplit=1)
    print(splitlist)

    #re.finditer()函数，返回匹配结果的迭代类型，每个元素都是match类型。
    for m in re.finditer(r"[1-9]\d{5}","BIT100081 BUT100045 NTU100035"):
        if m:
            print(m.group(0))

    #re.sub()函数，替换匹配的部分，返回替换后的列表
    sublist = re.sub(r"[1-9]\d{5}",":Tom","BIT100081 BUT100045 NTU100035")
    print(sublist)

    #正则表达式面对对象的等价用法
    pat = re.compile(r"[1-9]\d{5}")#编译正则表达式
    rst = pat.search("BIT100081 BUT100045 NTU100035")#编译后直接.函数操作
    if rst:
        print(rst.group(0))

    findalllist_1 = pat.findall("BIT100081 BUT100045 NTU100035")
    print(findalllist_1)

if 0:#match类型介绍
    import re
    match = re.search(r"[1-9]\d{5}","BTU100032 POI100034")
    if match:
        print(match)
        print("-"*100)
        #match对象的属性
        print(match.string)
        print(match.re)
        print(match.pos)
        print(match.endpos)
        print("-"*100)
        #match对象的方法
        print(match.group(0))
        print(match.start())
        print(match.end())
        print(match.span())
    print(type(match))

if 0: #贪婪匹配和最小匹配
    import re
    m = re.search(r"PY.*N","PYANBNCNDN")
    print(m.group(0))# re库默认采用贪婪匹配，即输出最长的子串
    #最短子串输出方式
    m_1 = re.search(r"PY.*?N","PYANBNCNDN")
    print(m_1.group(0))

