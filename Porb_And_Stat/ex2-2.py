import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

data = pd.DataFrame((0.5+np.random.randn(10,2)*0.1)*100)
score = data[0]*0.2 + data[1]*0.8
data = pd.concat([data[0], data[1], score],axis=1, keys=["A", "B", "Final"])
data.to_excel("final.xlsx")
data.to_csv("final.txt",index=False, float_format='%.2f', sep="\t")

plt.hist(score, label="final score", bins=10)
plt.legend()
plt.savefig("final.png")

file = open("final.txt","a")
file.write("* 최종점수 평균과 표준편차\n")
file.write(str([np.mean(data.Final),np.std(data.Final)]))
file.close()