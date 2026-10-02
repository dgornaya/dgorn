#!/usr/bin/python3
a = list(map(int,input().split()))
for x in a:
    print(x)
a.sort(reverse=True)
for x in a:
    print(x)
