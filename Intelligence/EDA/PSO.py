import math

import numpy as np

arr=[[2,1,3000000,0.0020],[5,2,5000000,0.0015],[9,1,17000000,0.0020]]

def cacFit(loc):
    for i in range(len(arr) - 1):
        tmp = arr[i]
        x = int(loc[0]) - int(tmp[0])
        y = int(loc[1]) - int(tmp[1])
        dis = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        r = float((tmp[3]))
        v = int(tmp[2])
        res = 0
        res += v * r * dis
    return res

def getweight():
    weight = 0.9
    return weight

def getlearningrate():
    lr = (0.49445,1.49445)
    return lr

def getmaxgen():
    maxgen = 300
    return maxgen

def getsizepop():
    sizepop = 20
    return sizepop

def getrangepop():
    rangepop = (-10,10)
    return rangepop

def getrangespeed():

    rangespeed = (-1,1)
    return rangespeed

def func(x):
    res = cacFit(x)
    return res

def initpopvfit(sizepop):
    pop = np.zeros((sizepop,2))
    v = np.zeros((sizepop,2))
    fitness = np.zeros(sizepop)

    for i in range(sizepop):
        pop[i] = [(np.random.rand()-0.5)*rangepop[0]*2,(np.random.rand()-0.5)*rangepop[1]*2]
        v[i] = [(np.random.rand()-0.5)*rangepop[0]*2,(np.random.rand()-0.5)*rangepop[1]*2]
        fitness[i] = func(pop[i])
    return pop,v,fitness

def getinitbest(fitness,pop):
    gbestpop,gbestfitness = pop[fitness.argmax()].copy(),fitness.max()
    pbestpop,pbestfitness = pop.copy(),fitness.copy()

    return gbestpop,gbestfitness,pbestpop,pbestfitness

w = getweight()
lr = getlearningrate()
maxgen = getmaxgen()
sizepop = getsizepop()
rangepop = getrangepop()
rangespeed = getrangespeed()

pop, v, fitness = initpopvfit(sizepop)
gbestpop, gbestfitness, pbestpop, pbestfitness = getinitbest(fitness, pop)

result = np.zeros(maxgen)
for i in range(maxgen):
        for j in range(sizepop):
            v[j] += lr[0]*np.random.rand()*(pbestpop[j]-pop[j])+lr[1]*np.random.rand()*(gbestpop-pop[j])
        v[v<rangespeed[0]] = rangespeed[0]
        v[v>rangespeed[1]] = rangespeed[1]

        for j in range(sizepop):
            pop[j] += 0.5*v[j]
        pop[pop<rangepop[0]] = rangepop[0]
        pop[pop>rangepop[1]] = rangepop[1]

        for j in range(sizepop):
            fitness[j] = func(pop[j])

        for j in range(sizepop):
            if fitness[j] < pbestfitness[j]:
                pbestfitness[j] = fitness[j]
                pbestpop[j] = pop[j].copy()

        if pbestfitness.min() < gbestfitness :
            gbestfitness = pbestfitness.min()
            gbestpop = pop[pbestfitness.argmax()].copy()

        result[i] = gbestfitness

print(result)
