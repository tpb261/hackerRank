#!/usr/bin/python3

h=int(input())
m=int(input())

n_to_s=["one"\
        , "two"\
        , "three"\
        , "four"\
        , "five"\
        , "six"\
        , "seven"\
        , "eight"\
        , "nine"\
        , "ten"\
        , "eleven"\
        , "twelve"\
        , "thirteen"\
        , "fourteen"\
        , "quarter"\
        , "sixteen"\
        , "seventeen"\
        , "eighteen"\
        , "nineteen"\
        , "twenty"\
        , "twenty one"\
        , "twenty two"\
        , "twenty three"\
        , "twenty four"\
        , "twenty five"\
        , "twenty six"\
        , "twenty seven"\
        , "twenty eight"\
        , "twenty nine"\
        ]

min=" minutes"
if(m==0):
    h_m_string = n_to_s[h-1]+" o' clock"
elif(30>m):
    if(m == 1):
        min=" minute"
    elif(m==15):
        min=""
    h_m_string = n_to_s[m-1]+min+" past "+n_to_s[h-1]
elif(30==m):
    h_m_string = "half past "+n_to_s[h-1]
elif(30<m):
    h+=1
    if(15 == 60-m):
        min=""
    h_m_string = n_to_s[60-m-1]+min+" to "+n_to_s[h-1]
print(h_m_string)
