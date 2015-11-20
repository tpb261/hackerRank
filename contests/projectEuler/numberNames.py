#!/usr/bin/python3
name={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight"\
      , 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen"\
      , 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"\
      , 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy"\
      , 80:"Eighty", 90:"Ninety", 100:"Hundred", 1000:"Thousand", 1000000:"Million"\
      , 1000000000:"Billion", 1000000000000:"Trillion", -1:""}

def get2DigitName(N, suffix):
    S=''
    if(N>0 and N<1000):
        if(N//100>0):
            S=''.join([S, name[N//100], ' Hundred'])
            N=N%100
        if(N>20):
            S=''.join([S.strip(), ' ', name[N-N%10]])
            N=N%10
        if(0<N<=20):
            S=''.join([S.strip(), ' ', name[N]])
        S=''.join([S.strip(), ' ', name[suffix]])
    return S

T=int(input())
for t in range(T):
    S=''
    N=int(input())
    if(0 == N):
        print("Zero")
        continue
    if(N>=1e12):
        S=''.join([S.strip(), ' ', get2DigitName(N//int(1e12)%1000, int(1e12))])
    if(N>=1e9):
        S=''.join([S.strip(), ' ', get2DigitName(N//int(1e9)%1000, int(1e9))])
    if(N>=1e6):
        S=''.join([S.strip(), ' ', get2DigitName(N//int(1e6)%1000, int(1e6))])
    if(N>=1e3):
        S=''.join([S.strip(), ' ', get2DigitName(N//1000%1000, 1000)])
    S=''.join([S.strip(), ' ', get2DigitName(N%1000, -1)])
    print(S.strip())
