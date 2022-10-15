N=int(input())
a=[int(s) for s in input().split()]
P=int(input())
del a[P-1]
(Q, K)=[int(s) for s in input().split()]
a.insert(Q-1, K)
print(" ".join([str(x) for x in a]))
