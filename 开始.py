#猜数字游戏
import random
from  math import pi
import time

def instrtest(instr):
    if instr == 'y':
        guass = inptest(int(input('请输入一个数字：')))
        print('*********************************************************\n' * 50)
        return guass
    elif instr == 'n':
        rand1 = random.randint(0, 1000)
        rand2 = random.randint(0, 1000)
        guass = random.randint(min(rand1, rand2), max(rand1, rand2))
        return guass
    elif instr == 'r':
        ranscope1 = inptest(int(input('请输入一个数字：')))
        ranscope2 = inptest(int(input('请输入一个数字：')))
        small = min(ranscope1, ranscope2)
        big =  max(ranscope1, ranscope2)
        guass = random.randint(small,big)
        print('范围为({},{})'.format(small,big))
        return guass
    else:
        instr = input('请输入正确的字符:')
        instrtest(instr)

def inptest(inp):
    '判断输入的是否为数字'
    if isinstance( inp, int ):
        return inp
    else:
        inp = int(input('输入错误,请重新输入：'))
        inptest(inp)

instr = input('是否要输入一个数字让别人猜，否则使用随机数字(0至1000的整数)\n是输入y,否输入n,自定义范围输入r :')
guass = instrtest(instr)

print('开始猜数字')
inp = -pi

while inp != guass:
    inp = int(input('请输入一个数字 ：'))
    inptest(inp)
    if inp == guass:
        print('对了')
        time.sleep(4)
        break
    elif inp < guass:
        print('小了')
    elif inp > guass:
        print('大了')