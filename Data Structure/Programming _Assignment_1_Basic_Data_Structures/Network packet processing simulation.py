# python3
import numpy as np
import sys

[S, n] = list(map(int, sys.stdin.readline().split()))
a = []
f = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in a:

    [A, p] = i
    if len(f) == 0:
        f.append(A + p)
        print(A)
    else:
        u = 0
        num = len(f)
        while f[u] <= A:
            u += 1
            if u == num: break
        f = f[u:]
         

        if len(f) == S:
            print(-1)
        else:
            if len(f) == 0:
                f.append(A + p)
                print(A)
            else:
                t = max(A, f[-1])
                f.append(t + p)
                print(t)
