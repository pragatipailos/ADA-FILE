import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
time = n * np.log2(n)

plt.plot(n, time)
plt.title("Quick Sort - Best/Average Case O(n log n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
time = n**2

plt.plot(n, time)
plt.title("Quick Sort - Worst Case O(n^2)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()
