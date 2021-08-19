from numpy import half, single, double, longdouble
import numpy as np
from scipy.linalg import inv
from laplaciana import laplaciana

N = 10

H = laplaciana(N, half)
S = laplaciana(N, single)
D = laplaciana(N, double)
L = laplaciana(N, longdouble)


#print(np.linalg.inv(H).nbytes) -> error
print("Tamaño de memoria single numpy (bytes) = ", np.linalg.inv(S).nbytes)
print("Tamaño de memoria double numpy (bytes) = ", np.linalg.inv(D).nbytes)
#print(np.linalg.inv(L).nbytes) -> error


print("Tamaño de memoria half scipy (bytes) = ", inv(H).nbytes)
print("Tamaño de memoria single scipy (bytes) = ", inv(S).nbytes)
print("Tamaño de memoria double scipy (bytes) = ", inv(D).nbytes)
print("Tamaño de memoria longdouble scipy (bytes) = ", inv(L).nbytes)


