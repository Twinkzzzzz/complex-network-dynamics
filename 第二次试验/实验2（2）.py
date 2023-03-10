import numpy as np
from matplotlib import pyplot
import networkx as nx
from math import comb

N = 1000
K = 6
KK = 3
pyplot.rcParams.update({'font.size':15})
pyplot.rcParams['font.sans-serif']=['SimHei']

def draw(N, K, P): #构造网络并统计的方式
    Y = np.zeros((20))
    T = 100 #采样次数
    for i in range(T):
        WSG = nx.random_graphs.watts_strogatz_graph(N, K, P) #生成WS小世界网络
        tmp = nx.degree_histogram(WSG) #获取度分布
        tmp /= np.sum(tmp) #归一化
        for j in range(len(tmp)):
            Y[j] += tmp[j]
    Y /= T #多次采样求平均值
    X = np.arange(0, len(Y))
    if (P == 0): #全局耦合网络特殊处理
        X = [K]
        Y = [1]
    pyplot.scatter(X, Y)
    pyplot.plot(X, Y, label="P=" + str(P))

def get(N, K, P):
    Y = np.zeros((20))
    X = np.arange(0, len(Y))
    for k in range(KK,20):
        for n in range(max(k-K,KK)+1): #第二种重连的边的范围情况
            if(k-n-KK<0 or (k-2*n<0 and P==0) or (1-P==0 and K+2*n-k<0)): #删减不符合条件的迭代
                continue
            Y[k]+=comb(KK,n)*comb(KK,k-n-KK)*pow(P,k-2*n)*pow(1-P,K+2*n-k) #调用公式
    if (P == 0):
        X = [K]
        Y = [1]
    pyplot.scatter(X, Y)
    pyplot.plot(X, Y, "--",label="P=" + str(P))

def get2(N, K, P):
    Y = np.zeros((20))
    X = np.arange(0, len(Y))
    for k in range(KK,20):
        for n in range(min(k-KK,KK)+1): #第一种重连的边的范围情况
            if(k-n-KK<0 or (k-2*n<0 and P==0) or (1-P==0 and K+2*n-k<0)):
                continue
            Y[k]+=comb(KK,n)*comb(KK,k-n-KK)*pow(P,k-2*n)*pow(1-P,K+2*n-k)
    if (P == 0):
        X = [K]
        Y = [1]
    pyplot.scatter(X, Y)
    if (P==0.4):
        print(X)
        print(Y)
    pyplot.plot(X, Y, "--", label="P=" + str(P))

pyplot.title("两种方式的近似程度")
pyplot.yscale('log')
pyplot.xlim(0, 16)
pyplot.xlabel("K")
pyplot.ylim(0.00001, 1)
pyplot.ylabel("P")
pyplot.vlines(K, -1, 2, linestyles="dashed")
pyplot.text(K + 0.1, 0.5, "X=K")
pyplot.vlines(K / 2, -1, 2, linestyles="dashed")
pyplot.text(K / 2 + 0.1, 0.5, "X=K/2")
draw(N, K, 0)
draw(N, K, 0.1)
draw(N, K, 0.2)
draw(N, K, 0.4)
draw(N, K, 0.6)
draw(N, K, 0.9)
draw(N, K, 1)
get2(N, K, 0)
get2(N, K, 0.1)
get2(N, K, 0.2)
get2(N, K, 0.4)
get2(N, K, 0.6)
get2(N, K, 0.9)
get2(N, K, 1)
pyplot.legend()

pyplot.legend()
pyplot.show()