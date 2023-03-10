import numpy as np
import pandas as pd
from matplotlib import pyplot
np.set_printoptions(precision=4,suppress=True)
N=7
b=np.zeros((N,N),dtype=int)
b[0][[1,2,3,4,6]]=1
b[1][0]=1
b[2][[0,1]]=1
b[3][[1,2,4]]=1
b[4][[0,2,3,5]]=1
b[5][[0,4]]=1
b[6][4]=1

a=b.transpose()
eigenvalue,eigenvector=np.linalg.eig(a) #求出特征值和特征向量
lamda=np.real(eigenvalue[0]) #默认第一个为最大特征值
X=np.zeros((N),dtype=float)
for i in range(N):
    X[i]=np.real(eigenvector[i][0]) #取出所对应的特征向量
X=X/np.sum(X) #归一化
print("最大特征值:",end=" ")
print(round(lamda,4))
print("中心性分值:",end=" ")
print(X)

d=0.85
A=np.zeros((N,N),dtype=float)
for i in range(N):
    for j in range(N):
        A[i][j]=(1-d)/N+d*b[i][j]/(np.sum(b[i])) #构造状态转移概率矩阵
print("状态转移概率矩阵:")
print(A)
A=A.transpose()
eigenvalue,eigenvector=np.linalg.eig(A)  #求出特征值和特征向量
lamda=np.real(eigenvalue[0]) #默认第一个为最大特征值
X=np.zeros((N),dtype=float)
for i in range(N):
    X[i]=np.real(eigenvector[i][0]) #取出所对应的特征向量
X=X/np.sum(X)
Y=np.arange(1,N+1,1)
print("最大特征值:",end=" ")
print(round(lamda,4))
print("Markov链的平稳分布:",end=" ")
print(X)
pyplot.bar(Y,height=X) #画出直方图
pyplot.title("PageRank值",fontname="SimHei")
pyplot.show()