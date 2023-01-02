import math
import numpy

def sum_neq(m0,n,neq,f):
    X = 0
    for m in range(m0,neq[0]):
        X += f(m)
    for M in range1(len(neq),1): 
        for m in range1(neq[M],neq[M-1]+1):
            X += f(m)
    for m in range(neq[len(neq)-1]+1,n+1): #correct
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