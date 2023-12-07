import numpy as np
import math
A = np.array([[5,-4],[-4,5]])
b = np.array([-1,2])
x_0 = np.array([0,0])


def r(x_k,b,A):
    return np.subtract(b ,np.matmul(A,x_k))

def alpha(r_k, A):
    top = np.matmul(np.transpose(r_k), r_k);
    bottom = np.matmul(np.transpose(r_k),np.matmul(A,r_k))

    return float(top) / float(bottom)

def SteepestDecent(x_k, b, A):
    r_k = r(x_k,b,A)
    return np.add(x_k, np.multiply(alpha(r_k,A),r_k))

x_k_sd = x_0
x_k1_sd = np.array([10,10])
epsilon = 0.000001
i = 0
err_sd = 1

while err_sd > epsilon and i < 100:
    i += 1
    x_k1_sd = SteepestDecent(x_k_sd,b,A)
    err_sd = abs(np.linalg.norm(x_k1_sd, 2) - np.linalg.norm(x_k_sd, 2))
    x_k_sd = x_k1_sd

print(x_k_sd)
print(i)

#part 2

#r_k = r vector at current step
#ps = list of previous p vectors
#A = matrix
#x_0 = initial guess
#b = b
#return p at kth step
def calc_p(ps, A, x_k, b):
    r_k = r(x_k, b, A)
    rhs = [0.0,0.0]
    if len(ps) == 0:
        ps.append(r_k)
        return r_k
    for p_j in ps:
        coeff = float(np.matmul(np.transpose(p_j),np.matmul(A,r_k))) / float(np.matmul(np.transpose(p_j),np.matmul(A,p_j)))

        rhs = np.add(rhs, np.multiply(coeff, p_j))
    ps.append(rhs)
    return np.subtract(r_k, rhs)

#calculate alpha for gradient descent method
def alphaCGM(p_k, A, x_k, b):
    r_k = r(x_k, b, A)
    top = float(np.matmul(np.transpose(p_k), r_k))
    bottom = float(np.matmul(np.transpose(p_k),np.matmul(A, p_k)))
    
    return top / bottom

def CGM(ps,A,x_k,b):
    p_k = calc_p(ps,A,x_k,b)
    return np.add(x_k, np.multiply(alphaCGM(p_k,A,x_k,b), p_k))

#define variables for itration
r_0 = r(x_0,b,A)
x_k_cgm = x_0;
x_k1_cgm = np.array([10,10]) #arbitrarily large array
err_cgm = 1
j = 0
ps = []
while  err_cgm > epsilon:
    j += 1
    x_k1_cgm = CGM(ps, A, x_k_cgm, b)
    err_cgm = abs(np.linalg.norm(x_k1_cgm, 2) - np.linalg.norm(x_k_cgm, 2))
    x_k_cgm = x_k1_cgm
    

print(x_k1_cgm)
print(j)
