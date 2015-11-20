#include <stdio.h>
void main()
{
    int hist[26]={0,};
    char s[100]={0,};
    int T = 0;
    int c=0;
    int j;
    scanf ("%d", &T);
    for(c=0;c<T;c++)
    {
        int l_hist[26]={0,};
        scanf ("%s", s);
        for(j=0;s[j];j++)
            l_hist[s[j]-'a']=1;
        for(j=0;j<26;j++)
            hist[j]+=l_hist[j];        
    }
    for(c=j=0;j<26;j++)
    {
        if(hist[j]==T)
        {
            c++;
        }
    }
    printf ("%d\n", c);
}
