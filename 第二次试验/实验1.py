import numpy as np
from matplotlib import pyplot
from math import pow
from math import sqrt
from random import random
import networkx as nx

N=3000 #节点数
T=50 #对每一种设定的采样次数

def draw(N,C,Z):
    P=C*(pow(N,-Z))
    #P=0.5
    Q=sqrt(N*P*(1-P))
    #print(P)
    X=np.linspace(-4,8,240) #构造画图的坐标
    Y=np.zeros(len(X))

    for i in range(T):
        print(i)
        G=nx.random_graphs.erdos_renyi_graph(N,P) #生成ER随机网络
        A=np.array(nx.adjacency_matrix(G).todense()) #获取邻接矩阵

        eigenvalue,eigenvector=np.linalg.eig(A) #获取频谱
        eigenvalue=eigenvalue/Q #归一化
        tmp=np.zeros(len(X))

        for item in eigenvalue:
            array=np.asarray(X)
            index=(np.abs(array-item)).argmin() #对每个特征值，找到其最接近的横坐标结点
            tmp[index]+=1 #作用相当于计算密度
        tmp=tmp/np.sum(tmp) #求概率，归一化
        Y+=tmp
    Y/=T #多次采样求平均值，归一化
    pyplot.plot(X,Y,label="N="+str(N)+" Z="+str(Z)+" C="+str(C)+ " P="+str(P))

pyplot.rcParams.update({'font.size':20})
draw(N,0.5,1) #四种情况作图
draw(N,1,1)
draw(N,1,1.5)
draw(N,10,1)
pyplot.xlabel("λ/sqrt[Np(1-p)]")
pyplot.ylabel("ρ")
pyplot.legend()
pyplot.show()