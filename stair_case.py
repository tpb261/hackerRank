import ast
n = int(input())
s=""
for i in range(0, n):
    s="".join(["#", s])
    print(s.rjust(n))
