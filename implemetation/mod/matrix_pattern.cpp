#include<iostream>
#include<stdio.h>
using namespace std;
//l -- large matrix
//s -- small matrix
int IsMatrixExists(int** l,int row_l,int col_l,int** s,int row_s,int col_s)
{
    if(row_s == 0 || col_s == 0 || row_s>row_l || col_s>col_l)
    	return 0;
    bool flag;
    for(int i = 0;i <= row_l-row_s;i++){
	for(int j = 0;j <= col_l-col_s;j++){
	    flag = true;
	    for(int p = 0,x = i;p < row_s && flag;p++,x++)
		for(int q = 0,y = j;q < col_s && flag;q++,y++){
		    if(l[x][y] != s[p][q])
			flag = false;
		}
	    if(flag){
		return 1;
	    }
	}
    }
    return 0;
}

int** getmatrix(int r,int c)
{
    int** p =new int*[r];
    for(int i=0;i<r;i++)
	p[i] = new int[c];
    for(int i=0;i<r;i++)
    {
	unsigned long int N;
	scanf ("%lu", &N);
	for(int j=c-1;j+1;j--)
	{
	    p[i][j] = N%10;
	    N/=10;
	}
	for(int j=0;j<c;j++)
	{
	    cout<<p[i][j]<<",";
	}
	cout<<"\n";
    }
    return p;
}

int main1(){
    int row_l,col_l,row_s,col_s;
    cin>>row_l>>col_l;    
    int** a = getmatrix(row_l,col_l);
    cin>>row_s>>col_s;
    int** b = getmatrix(row_s,col_s);
    if(IsMatrixExists(a,row_l,col_l,b,row_s,col_s))
	cout<<"YES\n";
    else
	cout<<"NO\n";
    return 0;
}

int main()
{
    int T;
    cin>>T;
    for(T;T;T--)
	main1();
}
