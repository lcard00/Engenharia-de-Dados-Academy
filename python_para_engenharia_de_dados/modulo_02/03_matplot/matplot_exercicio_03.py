from matplotlib import pyplot as plt

x = ["Python", "C++", "Java", "Perl", "Scala", "Lisp"]
y = [10, 8, 6, 4, 2, 1]

plt.figure(figsize=(10, 8))
plt.bar(
    x,
    y,
    color="mediumslateblue",
    alpha=0.9,
    edgecolor="black",
    linewidth=0.6,
)
plt.ylabel("Usage")
plt.title("Programming language usage")
plt.ylim(0, 10)
plt.show()
