import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
best = n

plt.plot(n, best)
plt.title("Insertion Sort - Best Case O(n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
worst = n**2

plt.plot(n, worst)
plt.title("Insertion Sort - Worst Case O(n^2)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()
