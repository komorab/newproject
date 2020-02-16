#求调和级数的前n项和并输出最简分式
def prime(x, y):
    "计算x和y的最大公约数"
    while x != y:
        if x>y:
            x -= y
        elif x<y:
            y -= x
    return x

n=int(input("输入n:"))
a=1;b=1
sums=1;sumx=1
while b<=n:
    if b==1:
        b += 1
    else:
        sums = sums * b + sumx
        sumx = b * sumx
        a=prime(sums, sumx)
        sums = sums / a
        sumx = sumx / a
        b += 1
print(sums)
print("-"*len(str(sums)))
print(sumx)
#上三行输出最简分式