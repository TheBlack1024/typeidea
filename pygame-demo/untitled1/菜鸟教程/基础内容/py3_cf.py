

# 乘法表
# 正序
def zxcf():
    print("\t" * 8, "正序乘法表", end="")
    for x in range(1, 10):
        print()
        for y in range(1, 10):
            if x >= y:
                print("{0}x{1}={2}".format(x, y, x*y), end="\t")

    


# 倒叙
def dxcf():
    print("\t" * 8, "倒序乘法表", end="")
    for x in range(9, 0, -1):
        print()
        for y in range(9, 0, -1):
            if x >= y:
                print("{0}x{1}={2}".format(y, x, x*y), end="\t")
            else:
                print("\t", end="\t")
                                        

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")