from matplotlib import pyplot as plt

values = [15.0, 30.0, 45.0, 10.0]
labels = ["Frogs", "Hogs", "Dogs", "Logs"]
explode = [0, .1, 0, 0]
colors = ["blue", "orange", "green", "red"]

plt.figure(
    figsize= (7, 7)
)

plt.pie(
    values,
    labels= labels,
    explode= explode,
    autopct= "%.1f%%",
    shadow= True,
    startangle= 90.0,
    colors= colors
)

plt.show()