import math
import numpy

def sum_neq(m0,n,neq,f):
    X = 0
    lenneq = len(neq)
    for m in range(m0,neq[0]):
        X += f(m)
    if lenneq > 1:
        for M in range1(lenneq,1):
            if neq[M]-neq[M-1] > 1:
                for m in range1(neq[M],neq[M-1]+1):
                    X += f(m)
    for m in range(neq[lenneq-1]+1,n+1):
        X += f(m)
    return X

def crj_u(r,s,j):
    k = r+s+1

def sum_neq_ez(m0,n,neq,f): #computes unnecessary terms
    X = 0
    for m in range(m0, n+1):
        X += f(m)
    for m in range(0,len(neq)):
        X -= f(neq[m])
    return X