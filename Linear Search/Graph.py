import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
best = np.ones(100)

plt.plot(n, best)
plt.title("Linear Search - Best Case O(1)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1, 100, 100)
avg = n

plt.plot(n, avg)
plt.title("Linear Search - Average Case O(n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Time")
plt.show()
