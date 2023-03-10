#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

const int N=6;
int a[110][110],minl[110][110],vis[110];
double mins[110][110],Bv[110],Be[110][110],Tv[110],Te[110][110];

void addedge(int x,int y)
{
	a[x][y]=a[y][x]=1;
	return;
}

void dij(int o) //dijkstra�㷨�������Դ���·�� 
{
	memset(vis,0,sizeof(vis));
	vis[o]=1;
	for(int i=1;i<=N;++i) minl[o][i]=a[o][i];
	bool flag=1;
	int k;
	while(flag)
	{
		flag=0;
		k=0;
		for(int i=1;i<=N;++i)
		{
			if(vis[i] || (!minl[o][i])) continue;
			flag=1;
			if(!k || (k && minl[o][i]<minl[o][k])) k=i;
		}
		vis[k]=1;
		for(int i=1;i<=N;++i)
		{
			if(vis[i] || !a[k][i]) continue;
			if(minl[o][k]+1<minl[o][i] || !minl[o][i]) minl[o][i]=minl[o][k]+1;
		}
	}
	return;
}

void gets(int o,int d,int tmp,int len) //�������е��֮�����·������ 
{
	if(len>=minl[o][d])
	{
		if(tmp==d) 
		{
			mins[o][d]++;
			vis[d]=1;
			for(int i=1;i<=N;++i)
			{
				if(vis[i] && i!=o && i!=d) Tv[i]++;
				for(int j=i+1;j<=N;++j)
				{
					if(vis[i] && vis[j] && a[i][j] && !(i==o && j==d || i==d && j==o)) Te[i][j]++;
				}
			}
			vis[d]=0;
		}
		return;
	}
	else
	{
		vis[tmp]=1;
		for(int i=1;i<=N;++i)
		{
			if(a[tmp][i] && !vis[i]) gets(o,d,i,len+1);
		}
		vis[tmp]=0;
	}
	return;
}

int main()
{
	memset(a,0,sizeof(a));
	memset(minl,0,sizeof(minl));
	memset(mins,0,sizeof(mins));
	memset(Bv,0,sizeof(Bv));
	memset(Be,0,sizeof(Be));
	addedge(1,2);
	addedge(1,3);
	addedge(1,5);
	addedge(2,3);
	addedge(2,4);
	addedge(3,6);
	addedge(4,6);
	for(int i=1;i<=N;++i) dij(i); //��ÿ������dijkstra�㷨����������е��֮������·��
	cout << "���֮�����·��:\n";
	for(int i=1;i<=N;++i)
	{
		for(int j=1;j<=N;++j)
		{
			cout << minl[i][j] << " ";
		}
		cout << endl;
	} 
	for(int i=1;i<=N;++i)
	{
		for(int j=i+1;j<=N;++j)
		{
			if(minl[i][j]) //ÿ������һ�����յ�ʱ���Ϳ���Ϊ���е�ͱ߼��������һ���� 
			{
				memset(vis,0,sizeof(vis));
				memset(Te,0,sizeof(Te));
				memset(Tv,0,sizeof(Tv));
				gets(i,j,i,0);
				for(int k=1;k<=N;++k)
				{
					Tv[k]/=mins[i][j];
					Bv[k]+=Tv[k];
					for(int p=k+1;p<=N;++p)
					{
						Te[k][p]/=mins[i][j];
						Be[k][p]+=Te[k][p];
					}
				}
			}
		}
	}
	cout << "���֮�����·������:\n";
	for(int i=1;i<=N;++i)
	{
		for(int j=1;j<=N;++j)
		{
			cout << minl[i][j] << " ";
		}
		cout << endl;
	}
	cout << "��Ľ���:\n";
	for(int i=1;i<=N;++i) cout << "vertice " << i << ": " << Bv[i] << endl;
	cout << "�ߵĽ���:\n";
	for(int i=1;i<=N;++i)
	{
		for(int j=i+1;j<=N;++j)
		{
			if(a[i][j]) cout << "edge(" << i << "," << j << "): " << Be[i][j] << endl;
		}
	}
	return 0;
}
