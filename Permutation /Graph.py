import matplotlib.pyplot as plt
import numpy as np
import math

n = np.arange(1, 8)   
time = [math.factorial(i) for i in n]

plt.plot(n, time)
plt.title("Time Complexity of Permutation Generation O(n!)")
plt.xlabel("n")
plt.ylabel("n!")
plt.show()
