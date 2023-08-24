import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-24/Desktop/data set mn/tips.csv")
print(data)
plt.scatter(data['day'],data['tip'])
plt.xlabel('daay')
plt.ylabel('tip')
plt.title('scatter')
plt.show()

