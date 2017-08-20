import random
import math
import numpy as np

price = np.array([55, 10, 47, 5, 4, 50, 8, 61, 85, 87])
weight = np.array([95, 4, 60, 32, 23, 72, 80, 62, 65, 46])
Count = 269

def best(pop, fitvalue): #找出适应函数值中最大值，和对应的个体
    px = len(pop)
    bestindividual = pop[0]
    bestfit = fitvalue[0]
    for i in range(px):
        if(fitvalue[i] > bestfit):
            bestfit = fitvalue[i]
            bestindividual = pop[i]
    return [bestindividual, bestfit]


def calfitvalue(pop): #计算目标函数值
    fitvalue = [];
    for i in range(len(pop)):
        fit = fitness(pop[i])
        fitvalue.append(fit)
    return fitvalue # 目标函数值objvalue[m] 与个体基因 pop[m] 对应

def calmoney(fitlist):
    #打印选择商品列表
    #print(fitlist)
    money = -1
    if(len(fitlist) ==10):
        money = price.dot(np.array(fitlist).T)
    return money

def fitness(goods):
    li = list()
    good = np.array(goods)
    fit = good.dot(weight.T)
    return fit

# 个体间交叉，实现基因交换
def crossover(pop, pc):
    poplen = len(pop)
    for i in range(poplen - 1):
        if(random.random() < pc):
            cpoint = random.randint(0, len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0 : cpoint])
            temp1.extend(pop[i+1][cpoint : len(pop[i])])
            temp2.extend(pop[i+1][0 : cpoint])
            temp2.extend(pop[i][cpoint : len(pop[i])])
            pop[i] = temp1
            pop[i+1] = temp2

# 基因突变
def mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])

    for i in range(px):
        if (random.random() < pm):
            mpoint = random.randint(0, py - 1)
            if (pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1

def sum(fitvalue):
    total = 0
    for i in range(len(fitvalue)):
        total += fitvalue[i]
    return total

def cumsum(fitvalue):
    newfit = []
    for i in range(len(fitvalue)):
        t = 0
        j = 0
        while(j <= i):
            t += fitvalue[j]
            j = j + 1
        newfit.append(t)
    for j in range(len(fitvalue)):
        fitvalue[j] = newfit[j]

# 自然选择（轮盘赌算法）
def selection(fitvalue):
    global pop
    newfitvalue = []
    totalfit = sum(fitvalue)
    for i in range(len(fitvalue)):
        newfitvalue.append(fitvalue[i] / totalfit)

    cumsum(newfitvalue)
    ms = []
    poplen = len(pop)
    for i in range(poplen):
        ms.append(random.random()) #random float list ms
    ms.sort()
    fitin = 0
    newin = 0
    newpop = pop
    while newin < poplen:
        if(ms[newin] < newfitvalue[fitin]):
            newpop[newin] = pop[fitin]
            newin += 1
        else:
            fitin += 1
    pop = newpop


popsize = 100  # 种群的大小
chromlength = 10  # 基因片段的长度
pc = 0.6  # 两个个体交叉的概率
pm = 0.01  # 基因突变的概率
results = [[]]
bestindividual = []
bestfit = 0
fitvalue = []
tempop = [[]]
pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] for i in range(popsize)]
for i in range(100):  # 繁殖100代
    fitvalue = calfitvalue(pop) # 计算个体的适应值
    [bestindividual, bestfit] = best(pop, fitvalue)  # 选出最好的个体和最好的函数值
    results.append([bestfit, calmoney(bestindividual)])  # 每次繁殖，将最好的结果记录下来
    selection(fitvalue)  # 自然选择，淘汰掉一部分适应性低的个体
    crossover(pop, pc)  # 交叉繁殖
    mutation(pop, pc)  # 基因突变

#results.sort()
file = open("C:\\Users\gq\Desktop\\gen.txt", "w")
# 打印函数最大值和对应的
for i in results:
    if(len(i) != 0):
        print(i[1])
       # file.write(str(i[1])+",")
file.close()