import numpy as np
from scipy import stats

x = np.random.rand(5)*100
print(np.sort(x))
print(np.average(x,weights=[0.1,0.2,0.4,0.2,0.1]))
print(stats.trim_mean(x,0.2))