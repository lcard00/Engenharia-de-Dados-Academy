import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

seed = 0
sample = 1000

np.random.seed(seed)  # Para garantir que os resultados sejam reproduzíveis.
dates_range = pd.date_range("2000-01-01", "2000-01-31", freq="D")
sex_list = ["M", "F"]
brazilian_states = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins",
}

weekday_map = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

# 1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
#   1. Idade: números inteiros aleatórios ente 0 e 100 (inclusos).
age = np.random.randint(0, 101, sample)

#   2. Data: data aleatórias entre 01/01/2000 até 31/01/2000.
# start_date = "2000-01-01"
# random_dates = np.random.randint(0, 31, sample)
# dates = pd.to_datetime(random_dates, origin=start_date, unit="D").date

dates = np.random.choice(dates_range, sample)

#   3. Nota: Números decimais entre 0 e 1000.
grades = np.random.uniform(0, 1000.01, sample).round(2)

#   4. Sexo: Valores aleatórios de M e F.
sex = np.random.choice(sex_list, sample)

#   5. Estado: Valores aleatórios entre os estados do Brasil.
states_list = list(brazilian_states.keys())
states = np.random.choice(states_list, sample)

df = pd.DataFrame(
    {"age": age, "date": dates, "grade": grades, "sex": sex, "state": states}
)

# print(df.info())
# max_grade = df["grade"].idxmax()
# print(df.iloc[max_grade])

# 2. Utilizando pandas, realizze as seguintes alterações no dataset: (semente 0)
#   1. Transforme 20% das notas em valorres nulos, simulando alunos que não compareceram à prova,.
mask_sample = df.sample(frac=0.2, random_state=seed).index
df.loc[mask_sample, "grade"] = np.nan

#   2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
mask_nan = df["grade"].isna()
df.loc[mask_nan, "grade"] = 0.00

# # mask_grade0 = df["grade"] == 0.00
# # print(df[mask_grade0])

#   3. Remova alunos com idades infferiores a 18 anos e superiores a 80, simulando uma ffiltragem
#         automática do sistema para alunos com idades incosistentes.
mask_age = df["age"].between(18, 80)
df.drop(df[~mask_age].index, inplace=True)

# print(df.info())

#   4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior
#       a 600. Simulando uma correção automática.
# mask_grade = df["grade"] >= 600
# df.loc[mask_grade, "approved"] = True
# df.loc[~mask_grade, "approved"] = False

approved = lambda x: True if x >= 600 else False
df["approved"] = df["grade"].apply(approved)

# mask_approved = df["approved"] == True
# print(df.loc[~mask_approved])

#   5. Crie um campo novo indicando o dia da semana para todas as datas.
weekday = df["date"].dt.day_of_week
df["weekday"] = weekday

# print(df.sample(100))

# 3. Gere um relatório com os seguintes tópicos:
#   1. Tabela cruzada de participantes de cada sexo por estado.
ct_state_sex = pd.crosstab(df["state"], df["sex"], margins=True)
ct_state_sex = ct_state_sex.rename(columns={"All": "Total"})

print(ct_state_sex)

#   2. Gráfico de pizza da quantidade de aprovados por sexo e um de barras com a quantidade
#       de aprovados por estado
approved = df["approved"] == True

approved_by_sex = df[approved].groupby("sex")["approved"].count()

plt.figure(figsize=(8, 8))

plt.pie(
    approved_by_sex,
    explode=[0.01, 0.01],
    labels=approved_by_sex.index,
    autopct="%.2f%%",
    # shadow = True,
    startangle=90.0,
    colors=["tomato", "cornflowerblue"],
)

plt.title(label="Approved by gender", fontdict={"fontsize": 16})

plt.show()

# approved_by_state = df[mask_approved].groupby("state")["approved"].count()
# approved_by_state = approved_by_state.sort_values(ascending=False)

approved_by_state = df.loc[approved, "state"].value_counts(ascending=True)

plt.figure(figsize=(8, 10))

plt.barh(
    approved_by_state.index,
    approved_by_state,
    color="cornflowerblue",
    alpha=0.9,
    edgecolor="black",
    linewidth=0.6,
)

plt.grid(axis="x", alpha=0.25)
plt.xticks(np.arange(2, approved_by_state.max() + 1, 2))
plt.xlim(2, approved_by_state.max() + 1)
plt.xlabel("students")
plt.ylabel("State")
plt.ylim(-1, len(approved_by_state))
plt.title("Approved by state")
plt.show()

#   3. Gráfico de pontos de nota por idade, colorindo por sexo.
# mask_grade_by_age = df.groupby(["age", "sex"])["grade"].mean().round(2).reset_index()
# mask_grade_by_age = mask_grade_by_age.rename(columns= {"grade" : "mean_grade"})

mask_grade_by_age = df[approved]

plt.figure(figsize=(14, 8))

sns.scatterplot(
    data=mask_grade_by_age, x="age", y="grade", hue="sex", palette="Set1", alpha=0.6
)

plt.title("Approved students by age and gender")
plt.xticks(np.arange(15, 81, 5))
plt.xlim(15, 81)
plt.yticks(np.arange(600, 1001, 50))
plt.ylim(570, 1020)
plt.grid(True, alpha=0.2)
plt.show()

#         1. Gráfico de barras com a participação por dia da semana e por dia do mês
mask_weekday_amount = df["date"].drop_duplicates().dt.weekday.value_counts()
mask_weekday_sum = df["weekday"].value_counts()
average_students = (mask_weekday_sum / mask_weekday_amount).rename(weekday_map).reset_index()
average_students = average_students.rename(columns={"index": "weekday", "count" : "students"})

plt.figure(figsize=(10, 6))

sns.barplot(
    data=average_students,
    x="weekday",
    y="students",
    alpha=0.8,
    edgecolor="black",
    linewidth=0.6,
    orient="x",
)

plt.grid(True, axis="y", alpha=0.3)
plt.title("Average participation")
plt.ylim(9, 23)
plt.show()

mask_day = df["date"].dt.day.value_counts().sort_index(ascending=False).reset_index()
mask_day = mask_day.rename(columns={"date": "day", "count": "students"})

plt.figure(figsize=(10, 14))

sns.barplot(
    data=mask_day,
    x="students",
    y="day",
    alpha=0.8,
    edgecolor="black",
    linewidth=0.6,
    orient="h",
    order=mask_day["day"].index,
)

plt.grid(True, axis="x", alpha=0.3)
plt.title("Participation by day")
plt.ylim(0.1, 31)
plt.xlim(8, 28)
plt.xticks(np.arange(10, 29, 2))
plt.show()

# #         2. Gráfico de pontos das notas por dia da semana.
mask_grade_by_weekday = (
    df.groupby("weekday")["grade"].mean().round(2).rename(weekday_map).reset_index()
)

plt.figure(figsize=(12, 6))

sns.barplot(
    data=mask_grade_by_weekday,
    x="weekday",
    y="grade",
    alpha=0.8,
    edgecolor="black",
    linewidth=0.6,
    orient="x",
)

plt.grid(True, axis="y", alpha=0.3)
plt.title("Average grade by weekday")
plt.ylim(200, 500)
plt.show()

df["weekday_name"] = df["date"].dt.day_name()

plt.figure(figsize=(10, 6))

sns.stripplot(
    data=df,
    x="weekday_name",
    y="grade",
    hue="weekday",
    palette="bright",
    legend= False,
    alpha=0.6,
)

plt.title("Grade by weekday")
plt.xlabel("weekday")
plt.show()
# # 4. Salve um arquivo csv com as notas dos 100 melhores alunos ordenados da melhor nota para a pior.
mask_top100 = df.iloc[:, :-3].nlargest(100, "grade")

# print(mask_top100.sort_values("grade", ascending=False))

mask_top100.to_csv("sample_data/approved.csv", index=False)
