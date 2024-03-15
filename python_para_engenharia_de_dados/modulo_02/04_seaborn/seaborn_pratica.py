import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("diamonds")

plt.figure(figsize=(12, 12))

sns.scatterplot(
    data=df,
    x="carat",
    y="price",
    hue="clarity",
    size="depth",
    sizes=(1, 200),
    style="cut",
    
)

# sns.catplot(
#     data=df,
#     x="cut",
#     y="price",
#     kind="bar"
# )

plt.show()