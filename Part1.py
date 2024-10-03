import pandas as pd
import matplotlib.pyplot as plt

data = [8, 9, 7, 5, 9, 7, 4, 8, 6, 7, 6, 5, 4]

df = pd.DataFrame(data)

plt.hist(data, bins=9)

plt.xlabel("x час сна")
plt.ylabel("y количество ллюдей")
plt.title("гистограмма количества часов сна")

plt.show()
