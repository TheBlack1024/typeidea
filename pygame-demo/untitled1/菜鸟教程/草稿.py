
# coding=utf-8
def abd(text):
    try:
        text1 = text.lower()
        textlist = []
        e = 0

        for a in text1:
            textlist.append(a)

        for b in textlist[:]:
            d = 0
            for c in textlist[:]:
                if c == b :
                    d += 1
                    textlist.remove(b)
                else:
                    pass
            if d >1:
                e += 1
            else:
                pass
        print(e)
    except:
        print("错误")
abd("qqqwwweeertyuiop")

