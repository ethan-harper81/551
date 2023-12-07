import numpy as np
import math
import matplotlib.pyplot as plt

LA = np.linalg

np.set_printoptions(threshold = np.inf)

b = np.array([(0.5)*(math.cos(x)) for x in range(1,64)])

#matrix
A = np.array([[2 if x == i
                else -1 if (x - 1) == (i) 
                else -1 if (x+1) == (i)  
                else 0 for x in range(0,63)] for i in range(0,63)])

x_est = np.linalg.solve(A,b);

x_0 = np.array([i / 64 for i in range(1, 64)])

def calc_r(A, x_k, b):
    
    return np.subtract(b, np.matmul(A,x_k))

def calc_p(r_k, A, p_values):
    if not p_values:
        p_values.append(r_k)
        return r_k
    else:
        curr_sum = np.array([0.0 for i in range(1,64)])
        for p_j in p_values:
            top = float(np.matmul(np.transpose(p_j) , np.matmul(A,r_k)))
            bottom = float(np.matmul(np.transpose(p_j) , np.matmul(A,p_j)))
            term = np.multiply((top / bottom), p_j)
            curr_sum = np.add(curr_sum, term)
        p_k = np.subtract(r_k, curr_sum)
        p_values.append(p_k)
        return p_k
    
def calc_alpha(p_k, r_k, A):

    top = float(np.matmul(np.transpose(p_k),r_k))
    
    bottom = float(np.matmul(np.transpose(p_k), np.matmul(A,p_k)))
    return (top / bottom)

def ConjugateGradientMethod(A, x_k, b, p_values):
    r_k = calc_r(A, x_k, b)

    p_k = calc_p(r_k, A, p_values)

    alpha_k = calc_alpha(p_k, r_k, A)

    x_k1 = np.add(x_k , np.multiply(alpha_k,p_k))
    return x_k1


m = 63;
x_k = x_0
x_k1 = x_0
p_values = []

x_coordinates = []
y_coordinates = []
for i in range(0, m):
    x_k1 = ConjugateGradientMethod(A,x_k, b, p_values)
    x_coordinates.append(m)
    y_coordinates.append(math.log10(LA.norm(np.subtract(x_k1,x_est), np.inf)))

    x_k = x_k1

plt.scatter(x_coordinates, y_coordinates)
plt.show()
