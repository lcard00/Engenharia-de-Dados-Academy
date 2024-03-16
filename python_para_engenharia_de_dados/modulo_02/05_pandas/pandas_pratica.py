import pandas as pd


s = pd.Series(
    data=["maisena", "farinha", "açucar", "ovos", "manteiga", "castanha"],
    index=["i1", "i2", "i3", "i4", "i5", "i6"],
    name="ingredientes",
    # dtype= str,
)

# print(s.values)
# print(type(s.values))

# print(s.name)
# print(type(s.index))

# print(s.index)
# print(type(s.index))

# print(s[1:-1])

# print(s["i2": "i4"])

# s2 = pd.Series(
#     data= [200, 250, 100, 2, 150, 180],
#     index= ["maisena", "farinha", "açucar", "ovos", "manteiga", "castanha"],
#     name = "quantidade",
#     # dtype =,
# )

# # print(s2)

# df = pd.DataFrame(
#     {
#         "ingredientes": ["maisena", "farinha", "açucar", "ovos", "manteiga", "castanha"],
#         "quantidade": [200, 250, 100, 2, 150, 180],
#     },
#     index= ["i1", "i2", "i3", "i4", "i5", "i6"],
# )

# print(df)
# print(type(df))

# print(df.index)
# print(df.columns)

# print(df.loc["i4", "quantidade"])

# df.iloc[3, 1] = 3

# print(df)

# print(df.dtypes)

# print(df["quantidade"])

df = pd.read_csv("sample_data/california_housing_train.csv")

# print(df.T)
# print(df.head(10))
# print(df.tail())
# print(df.info())

df.loc[100:1099, "longitude"] = None

# print(df.info())
# print(df.loc[50:150])
# print(df.isnull().sum())
# print(df.duplicated().any())
# df.drop_duplicates(inplace= True)

# print(df.sort_values("housing_median_age"))
# print(df.sort_values("housing_median_age", ascending= False))
# print(df.sort_index(ascending= False))

# print(df["housing_median_age"].nunique())
# print(df["housing_median_age"].unique())
# print(df["housing_median_age"].value_counts())#.sort_index())

# print(df.groupby("housing_median_age")["median_house_value"].max())
# print(df.groupby("housing_median_age")["median_house_value"].min())
# print(df.groupby("housing_median_age")["median_house_value"].mean())

df2 = (
    df.groupby("housing_median_age")["median_house_value"]
    .agg(["min", "mean", "max"])
    .round({"mean": 2})
)

# print(df2.melt())

# mask_age_gt15 = df["housing_median_age"] > 15

# print(df[mask_age_gt15])
# print(df[~mask_age_gt15])

# print(df[["longitude", "latitude"]])
# print(df.fillna("-1").iloc[50:150])
# print(df.describe())

# def age_days(idade):
#     idade_dias = idade * 365
#     return idade_dias

# print(df["housing_median_age"].apply(age_days))

# print(pd.crosstab(df["latitude"], df["housing_median_age"]))

# print(df.rename(columns={"longitude": "long", "latitude" : "lat"}, inplace=False))