import numpy as np
import matplotlib.pyplot as plt

m=20
n=3
X = np.random.rand(m, n)
mu=np.zeros_like(X[0,:])            # use np.zeros(n)
"""
print(mu)
print(X)
"""
for j in range(n):
            mu[j]=1/m*np.sum(X[:,j])

print(mu)    
for i in range(1,12,10):
        print(i)