#!/bin/python3

n,d=list(map(int,input().split(' ')))
arr = list(map(int,input().split(" ")))
d=d%n
for i in range(d,n):
    print(arr[i],end=' ')
for i in range(0,d):
    print(arr[i],end=' ')
