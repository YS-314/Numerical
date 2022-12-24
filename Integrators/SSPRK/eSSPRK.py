#explicit strong stability preserving Runge-Kutta methods (s,n) of stages s and order n
#integrates semi-discretised hyperbolic conservation laws of d/Udt = F(U)
#Uses Shu-Osher form of RK methods
import numpy as np
import math

#Shu-Osher (3,3)
class eSSP33():
    alpha = tri2darr(1,3/4,1/4,1/3,0,2/3)
    beta = tri2darr(1,0,1,0,0,1)
    s = 3
    p = 3
    adaptive = False
#eSSPRK(2,2)
class eSSP22():
    alpha = tri2darr(1,1/2,1/2)
    beta = tri2darr(1,0,1)
    s = 2
    p = 2
    adaptive = False
#eSSPRK(5,4)
class eSSP54():
    alpha = tri2darr(1,0.444370493651235,0.555629506348765,0.620101851488403,0,0.379898148511597,0.178079954393132,0,0,0.821920045606868,0,0,0.517231671970585, 0.096059710526147,0.386708617503268 )
    beta = tri2darr(0.391752226571890,0, 0.368410593050371,0,0,0.251891774271694,0,0,0,0.544974750228521,0,0,0,0.063692468666290,0.226007483236906) 
    s = 5
    p = 4
    adaptive = False

es_METHODS = {'eSR33': eSSP33,
           'eSR22': eSSP22,
           'eSR54': eSSP54}

def eSSP_int(func,t,U,tn,h,method='eSR33',kl=False):
    """
    1 step of eSSP integration
    func: callable function
    t: time value (np n dimensional array) 
    U: value of U (np n dimensional array)
    tn: end time
    h: (initial) stepsize 
    method: methods (default eSR33)
    ui: dictionary of u^i values
    kl: keep list of evaluations
    """
    #initialise
        if method in es_METHODS:
        method = es_METHODS[method]
    n = U.shape
    alpha = method.alpha
    beta = method.beta
    s = method.s
    adaptive = method.adaptive
    if adaptive = False:
            k = math.floor((tn-t)/h)
            for ti in range(k-2):
                U = eSSPstep_na(n,s,h,U,func,alpha,beta)
            U = eSSPstep_na(n,s,tn - hk,U,func,alpha,beta)

def eSSPstep_na(n,s,dt,U,func,alpha, beta):
    ui = np.zeros((s+1,)+(n))
    ui[0] = U
    for i in range(s-1):
        Xi = np.zeros(n)
        for j = range(i-1):
            Xi += alpha[i,j]*ui[j] + dt*beta[i,j]func(ui[j])


