import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 11)  


moves = 2**n - 1


plt.figure(figsize=(8, 5))
plt.plot(n, moves, marker='o', color='blue', label='T(n) = 2^n - 1')

plt.title("Tower of Hanoi Time Complexity")
plt.xlabel("Number of Disks (n)")
plt.ylabel("Number of Moves")
plt.grid(True)
plt.legend()

plt.show()
