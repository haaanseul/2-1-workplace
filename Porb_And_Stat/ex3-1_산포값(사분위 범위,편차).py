import numpy as np
import pandas as pd

x = np.random.rand(5)
print(np.percentile(x,[25,50,75]))

data = pd.DataFrame(x)
q1 = data.quantile(0.25)
q2 = data.quantile(0.50)
q3 = data.quantile(0.75)
print(q1)
print(q2)
print(q3)
print(data.describe())
print((q3-q2)/2)