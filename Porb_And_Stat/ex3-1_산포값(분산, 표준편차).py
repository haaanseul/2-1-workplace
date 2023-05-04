import numpy as np

x = np.random.rand(5)
print(x)
print(sum((x-np.mean(x))**2)/(len(x)-1))
print(np.var(x, ddof=1), np.std(x, ddof=1))

print(sum((x-np.mean(x))**2)/len(x))
print(np.var(x, ddof=0), np.var(x))
print(np.sqrt(np.var(x)), np.std(x))