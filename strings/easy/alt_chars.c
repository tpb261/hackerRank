#include<stdio.h>
char s[100000]={0,};

int main()
{
    int T;
    scanf ("%d", &T);
    for(;T; T--)
    {
	int j, d=0;
	scanf ("%s", s);
	for(j=1; s[j];j++)
	{
	    int k = j;
	    for(;s[j-1]==s[j] && s[j]; j++);
	    d+=(j-k);
	    if(!s[j]) break;
	}
	printf ("%d\n", d);
    }
    
}
