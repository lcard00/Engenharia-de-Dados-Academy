from matplotlib import pyplot as plt
import numpy as np

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
temp = [29, 26, 25, 20, 18, 17, 16, 18, 19]

plt.figure(
    figsize= (15, 10)
)

plt.plot(
    month, 
    temp,
    color= "red"
)

plt.yticks(
    [0, 10, 20, 30, 40]
)

plt.ylim(
    [0, 40]
)

plt.xlabel(
    "Months"
)

plt.ylabel(
    "°C"
)

plt.title(
    "Temperatures in 2023"
)

plt.grid(
    axis= "y"
)

plt.legend(
    "temp"
);


# plt.show()





