import numpy as np
import statistics as st

x = np.random.rand(5)*100
print(x)
print(5/(1/x[0]+1/x[1]+1/x[2]+1/x[3]+1/x[4]))
print(st.harmonic_mean(x))