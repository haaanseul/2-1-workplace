import numpy as np
import statistics as st

x = np.random.rand(5)*100
print(x)
print((x[0]*x[1]*x[2]*x[3]*x[4])**(1/5))
print(st.geometric_mean(x))