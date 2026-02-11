import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 10, 10)

time = 2**n

plt.plot(n, time)

plt.title("Time Complexity of Truth Table Generation")
plt.xlabel("Number of Variables (n)")
plt.ylabel("Time (2^n)")

plt.show()
