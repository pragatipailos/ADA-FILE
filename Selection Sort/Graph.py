import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)

time = n**2

plt.plot(n, time)

plt.title("Time Complexity of Selection Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (n^2)")

plt.show()
