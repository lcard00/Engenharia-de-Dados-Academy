from tracemalloc import start
import pandas as pd
import numpy as np

np.random.seed(0)  # Para garantir que os resultados sejam reproduzíveis.

# 1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
#   1. Idade: números inteiros aleatórios ente 0 e 100 (inclusos).
age = np.random.randint(0, 101, 1000)

#   2. Data: data aleatórias entre 01/01/2000 até 31/01/2000.
start_date = "2000-01-01"
random_dates = np.random.randint(1, 32, 1000)
dates = pd.to_datetime(random_dates, origin=start_date, unit="D").date

#   3. Nota: Números decimais entre 0 e 1000.
grades = np.random.uniform(0, 1000.01, 1000).round(2)

#   4. Sexo: Valores aleatórios de M e F.
sex = np.random.choice(["M", "F"], 1000)

#   5. Estado: Valores aleatórios entre os estados do Brasil.
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

states_list = list(brazilian_states.keys())
states = np.random.choice(states_list, 1000)

df = pd.DataFrame(
    {"age": age, "date": pd.to_datetime(dates), "grade": grades, "sex": sex, "state": states}
)

# max_grade = df["grade"].idxmax()
# print(df.iloc[max_grade])

# 2. Utilizando pandas, realizze as seguintes alterações no dataset: (semente 0)
#   1. Transforme 20% das notas em valorres nulos, simulando alunos que não compareceram à prova,.

mask_sample = df.sample(frac=0.2).index
df.loc[mask_sample, "grade"] = np.nan

#   2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
mask_nan = df["grade"].isna()
df.loc[mask_nan, "grade"] = 0.00

# mask_grade0 = df["grade"] == 0.00
# print(df[mask_grade0])

#   3. Remova alunos com idades infferiores a 18 anos e superiores a 80, simulando uma ffiltragem
#         automática do sistema para alunos com idades incosistentes.
mask_age = df["age"].between(18, 80)
df.drop(df[~mask_age].index, inplace=True)
# print(df.info())

#   4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior
#       a 600. Simulando uma correção automática.
mask_grade = df["grade"] >= 600
df.loc[mask_grade, "approved"] = True
df.loc[~mask_grade, "approved"] = False

# mask_approved = df["approved"] == True
# print(df.loc[~mask_approved])

#   5. Crie um campo novo indicando o dia da semana para todas as datas.
weekday = df["date"].dt.day_name()
df["weekday"] = weekday

# print(df.sample(100))

# 3. Gere um relatório com os seguintes tópicos:
#   1. Tabela cruzada de participantes de cada sexo por estado.
#   2. Gráffico de pizza da quantidade de aprovados por sexo e um de barras com a quantidade de aprovados por estado
#   3. Gráfico de pontos de uma nota por idade, colorindo por sexo.
#         1. Gráfico de barras com a participação por dia da semana e por dia do mês.add()
#         2. Gráfico de pontos das notas por dia da semana.

# 4. Salve um arquivo csv com as notas dos 100 melhores alunos ordenados da melhor nota para a pior.
