# estimation of distribution to solve package question
import numpy as np
import math
from numpy import random

price = np.array([55, 10, 47, 5, 4, 50, 8, 61, 85, 87])
weight = np.array([95, 4, 60, 32, 23, 72, 80, 62, 65, 46])
# 初始化种群数量，可以改进用input()
popSize = 1000
# 初始化物品数量
size = 10
# 背包的容量，可以动态指定
Count = 269
# 记录代数的全局变量，初始化为0代
generation = 0
# 打开两个文件用于存储在进化过程中每一代的最大值和平均值
fileMax = open("C:\\Users\gq\Desktop\\max.txt", "w")
fileAvg = open("C:\\Users\gq\Desktop\\average.txt", "w")
# 初始化价格数组
def getPrive(path):
    price1 = np.genfromtxt(path, dtype=float, delimiter=",")
    return price1

def getWeight(path):
    weight1 = np.genfromtxt(path, dtype=float, delimiter=",")
    return weight1

# 求适应度函数
def fitness(goods):
    li = list()
    w = 0.0
    p = 0.0
    M = 5000 # 参数M

    for i in range(len(goods)):
        if goods[i] == 1:
            li.append(i)
    for j in range(len(li)):
        index = li[j]
        p += float(price[index])
        w += float(weight[index])
    cw = Count - w
    if cw > 0:
        cw = 0
    else:
        cw = M * math.pow(cw, 2)
    fit1 = p * -1 + cw
    return fit1

# 初始化种群函数
def createPop(popsize,size):
    pro = np.zeros(size)
    goodlist = np.zeros((popsize, size))

    # 初始化概率均为0.5
    pro.fill(0.5)
    # 初始化种群的商品列表
    for j in range(popsize):
        for k in range(size):
            if np.random.rand() > 0.5:
                goodlist[j][k] = 1

    return pro, goodlist

# 调用 createPop()函数，初始化种群
pro, goodlist = createPop(popSize, size)

def changePop(): #种群进化
    n = int(popSize * 0.2)
    select = np.zeros((n, size))
    order = np.zeros(popSize, dtype=[('x', int), ('y', float)])
    index = 0
    global pro

    # 首先计算每个个体的适应度，然后按照适应度大小对个体进行排名
    for l in range(popSize):
        order[l][0] = l
        order[l][1] = fitness(goodlist[l])
    order.sort(order='y')

    for i in order.getfield(np.int):
        select[index] = goodlist[i]
        index += 1
        if index >= n:
            break
    # 根据 评估每个变量的概率，重新生成变量的概率值
    pro = select.sum(axis=0)/n

# 进化生成下一代种群函数
def evolution():
    goods = np.zeros((size))
    # 根据新的概率，生成下一代种群
    for j in range(popSize):
        for i in range(size):
            if random.rand() < pro[i]:
                goods[i] = 1
            else:
                goods[i] = 0
        goodlist[j] = goods
    money = price.dot(goodlist.T)
    max = money.max()
    average = money.sum()/popSize

    global generation
    generation += 1

    fileMax.write(str(generation)+',' + str(max))
    fileAvg.write(str(generation)+',' + str(average))
    fileMax.write("\n")
    fileAvg.write("\n")

def eda(genes):
    for g in range(genes):
        changePop()
        evolution()
    # 将最后一代种群中个体的商品列表写到文件中
    goodlist[popSize - 1].tofile("C:\\Users\gq\Desktop\goods.txt", sep=",")

if __name__ == '__main__':
    eda(20)
    fileMax.close()
    fileAvg.close()




