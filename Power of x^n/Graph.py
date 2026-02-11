import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
time = n

plt.plot(n, time)
plt.title("Time Complexity of Power Function (O(n))")
plt.xlabel("n")
plt.ylabel("Time")
plt.show()
