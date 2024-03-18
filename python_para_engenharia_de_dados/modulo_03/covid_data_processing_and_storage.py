import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from sqlalchemy import create_engine, text

def get_data(path):
    df = pd.read_csv(path)
    return df

def save_to_database(engine, df):
    df.to_sql(
        "confirmados_obito", 
        con=engine, 
        index=False, 
        if_exists="replace"
    )

db = "sqlite:///files/covid19_world.db"

df = get_data("files/cleaned_covid19_world.csv")

# print(df)

confirmados = df[["pais", "total_confirmados"]].nlargest(10, "total_confirmados")

plt.figure(figsize=(10, 5))

sns.barplot(
    confirmados,
    x="total_confirmados",
    y="pais",
    hue="total_confirmados",
    palette="Blues_d",
    orient="h",
    linewidth=0.6,
    edgecolor="black",
    legend=False
)

plt.gca().xaxis.set_major_formatter(
    ticker.FuncFormatter(
        lambda x, _: '{:.0f}M'.format(x / 10**6)
    )
)

plt.title("Covid-19 Confirmados")
plt.xlabel("Total de casos confirmados")
plt.xlim(5000000, 105000000)
plt.xticks(np.arange(10000000, 105000000, 10000000))
plt.grid(axis="x", alpha=0.3)
plt.show()

obitos = df[["pais", "total_obitos"]].nlargest(10, "total_obitos")

plt.figure(figsize=(10, 5))

sns.barplot(
    obitos,
    x="total_obitos",
    y="pais",
    hue="total_obitos",
    palette="Reds_d",
    orient="h",
    linewidth=0.6,
    edgecolor="black",
    legend=False
)

plt.gca().xaxis.set_major_formatter(lambda x, _: '{:,.0f}'.format(x))

plt.title("Covid-19 Óbitos Confirmados")
plt.xlabel("Total de óbitos confirmados")
plt.xlim(50000, 1150000)
plt.xticks(np.arange(100000, 1150000, 100000), rotation=25)
plt.grid(axis="x", alpha=0.3)
plt.show()

engine = create_engine(db)

save_to_database(engine, df)

# conn = engine.connect()
# result = conn.execute(
#     text(
#         "SELECT pais, \
#             total_confirmados \
#         FROM confirmados_obito \
#         ORDER BY total_confirmados DESC \
#         LIMIT 10"
#     )
# )
# conn.close()
# new_df = pd.DataFrame(result.fetchall())
# print(new_df)

engine.dispose()
