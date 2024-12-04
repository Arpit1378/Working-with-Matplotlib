import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1,2,3,4,5,6]
y = [56,22,12,30,4,15]

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(x,y,color=['Blue','Red','Orange','Black','Pink','Green'])
plt.show()