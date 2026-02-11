import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
time = n * np.log2(n)

plt.plot(n, time)
plt.title("Merge Sort - Time Complexity O(n log n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()
