
# coding=utf-8

if 0:
    # 递归函数使用示例
    def recur_fibo(n):
        """递归函数
        输出斐波那契数列"""
        if n <= 1:
            return n
        else:
            return (recur_fibo(n - 1) + recur_fibo(n - 2))


    # 获取用户输入
    nterms = int(input("您要输出几项? :"))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):
            print(recur_fibo(i+1))
if 0:
    a = "I like superman!"
    b = a.split(" ",4)
    for i in b:
        print(i)



