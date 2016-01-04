#include <iostream>
#include <vector>
using namespace std;

struct element{
    int row,col,value;
};

int countLength(int highC,int highR,int lowC,int lowR,vector <element> &v){
    
    int a = lowC,b = lowR,count=0;
    struct element e;
    e.row = a;
    e.col = b;
    v.push_back(e);
     do{
        count++;
        a++;
        e.row = a;
        e.col = b;
        v.push_back(e);
     }while (a<highR);
    do{
        count++;
        b++;
        e.row = a;
        e.col = b;
        v.push_back(e);
    }while (b<highC);
    do{
        count++;
        a--;
        e.row = a;
        e.col = b;
        v.push_back(e);
    }while (a>lowR);
     do{
        count++;
        b--;
         e.row = a;
         e.col = b;
         v.push_back(e);
     }while (b>lowC);
    return count;
}

void changeMatrix(int arr[][300],int highC,int lowC,int highR,int lowR,int r,int c,int k){
    
    vector<element> v;
    int len = countLength(highC,highR,lowC,lowR,v);
    if(k<0){
		k = (-k)%len;
		k = len -k;
    }
    k = k%len;
    v.pop_back();
    
    for (int i=0; i<v.size();i++) {
        int n = (i+k)%len;
        v[n].value = arr[v[i].row][v[i].col];
    }
    
    for (int i=0; i<v.size(); i++) {
        int r = v[i].row;
        int c = v[i].col;
        arr[r][c] = v[i].value;
    }
    
}

int main(int argc, const char * argv[]) {
    
    int r,c,k,arr[300][300];
    cin>>r>>c>>k;
    for (int i=0; i<r; i++) {
	int N;
        for (int j=0; j<c; j++) {
            cin>>arr[i][j];
	    //=N%10;	    N/=10;
        }
    }
    int highC=c-1,highR=r-1,lowC=0,lowR=0;
    while (true) {
        
        if (highC-lowC<1||highR-lowR<1) {
            break;
        }
        else{
            changeMatrix(arr,highC,lowC,highR,lowR,r,c,k);
        }
        highC--;
        highR--;
        lowC++;
        lowR++;
    }
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }
}
