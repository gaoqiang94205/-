import matplotlib.pyplot as plt

def plotMax():
    file = open('C:\\Users\gq\Desktop\\max.txt', 'r')
    lineslist = file.readlines()
    lineslist = [line.strip().split(",") for line in lineslist]
    file.close()
    x = [x[0] for x in lineslist]
    print(x)
    y = [x[1] for x in lineslist]
    print(y)
    plt.plot(x, y, 'b*')
    plt.plot(x, y, 'r')
    plt.legend()

def plotMean():
    file = open('C:\\Users\gq\Desktop\\average.txt', 'r')
    linesList = file.readlines()
    linesList = [line.strip().split(",") for line in linesList]
    file.close()
    x = [x[0] for x in linesList]
    print(x)
    y = [x[1] for x in linesList]
    print(y)
    plt.plot(x, y, 'b*')
    plt.plot(x, y, 'r')
    plt.xlabel("generation --x")
    plt.ylabel("average and max of value when N=1000")
    plt.ylim(0, 400)
    plt.title('EDA algorithm to solve package question')
    plt.legend()
    plotMax()
    plt.show()
def plotGen():
    file = open('C:\\Users\gq\Desktop\\gen.txt', 'r')
    line = file.readline()
    y = line.strip().split(",")
    ylist = []
    #for j in range(len(y) - 1):
    #    ylist.append(int(y[j]))
    file.close()
    ylist.sort(reverse=True)
    num = len(ylist)
    xlist = [x for x in range(num)]
    plt.plot(xlist, ylist, 'b*')
    plt.plot(xlist, ylist, 'r')
    plt.xlabel("generation --x")
    plt.ylabel("average and max of value when N=200")
    plt.ylim(0, 400)
    plt.title('gen algorithm to solve package question')
    plt.legend()
    plotMax()
    plt.show()

if __name__ == '__main__':
    plotMean()
    #plotGen()
