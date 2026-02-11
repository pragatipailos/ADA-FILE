import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)

time = n

plt.plot(n, time)

plt.title("Time Complexity of Horner's Rule")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (n)")

plt.show()
