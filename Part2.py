import pandas as pd
import matplotlib.pyplot as plt

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Диаграмма рассеивания")

plt.show()