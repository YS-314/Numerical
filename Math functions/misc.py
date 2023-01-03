
#Sum of f(x) for x from m0 to n excluding neq
'''
m0: start of sum (int)
n: end of sum (int)
neq: values to skip (1D list of int)
f: function to take sum of (callable)
'''
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

def prod_neq(m0,n,neq,f):
    X = 1
    lenneq = len(neq)
    for m in range(m0,neq[0]):
        X *= f(m)
    if lenneq > 1:
        for M in range1(lenneq,1):
            if neq[M]-neq[M-1] > 1:
                for m in range1(neq[M],neq[M-1]+1):
                    X *= f(m)
    for m in range(neq[lenneq-1]+1,n+1):
        X *= f(m)
    return X

#inputs same as sum_neq / prod_neq
#more naive implementation: computes unnecessary (skipped) terms. Not suitable if function is undefined at the points.
#Accuracy might be slightly lower than functions above due to floating point error caused by multiplying then dividing skipped terms
def sum_neq_2(m0,n,neq,f):
    X = 0
    for m in range(m0, n+1):
        X += f(m)
    for m in range(0,len(neq)):
        X -= f(neq[m])
    return X

def prod_neq_2(m0,n,neq,f):
    X = 1
    for m in range(m0, n+1):
        X *= f(m)
    for m in range(0,len(neq)):
        X /= f(neq[m])
    return X
