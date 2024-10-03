import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.cos(x)

plt.plot(x, y)  #
plt.xlabel("x")
plt.ylabel("y")
plt.title("График y = cos(x)")
plt.grid(True)
plt.show()  # plot


