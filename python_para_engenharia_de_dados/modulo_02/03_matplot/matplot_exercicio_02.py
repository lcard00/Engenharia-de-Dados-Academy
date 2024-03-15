from matplotlib import pyplot as plt
import numpy as np


x = [1.2, 2.4, 3.3, 4, 4.4, 5]
y = [63, 34, 22, 48, 18, 5]
x_range = np.arange(1.5, 5.5, 0.5)
y_range = np.arange(20, 61, 10)
size = np.array([10, 6, 3, 8, 2, 10]) * 15
colors = ["red", "green", "yellow", "yellow", "green", "red"]
# colors = [1, 5, 10, 10, 5, 1]

plt.figure(figsize=(6, 4), dpi=100)

plt.scatter(
    x=x,
    y=y,
    s=size,
    c=colors,
    # marker="P",
    # cmap="Set1",
    # alpha=0.6,
    # linewidths=100
)

plt.xticks(x_range)

plt.yticks(y_range)

plt.show()
