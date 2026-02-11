import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 1000, 100)
best = np.ones(100)

plt.plot(n, best)
plt.title("Binary Search - Best Case O(1)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 1000, 100)
time = np.log2(n)

plt.plot(n, time)
plt.title("Binary Search - O(log n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()
