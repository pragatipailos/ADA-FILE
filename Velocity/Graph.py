import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)

time = n

plt.plot(n, time)
plt.title("Time Complexity of Velocity with Bounce (O(n))")
plt.xlabel("Number of Steps (n)")
plt.ylabel("Time")
plt.show()
