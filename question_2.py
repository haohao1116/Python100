#计算阶乘

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

if __name__ == '__main__':
    x = int(input("请输入一个整数："))
    res = fact(x)
    print(res)