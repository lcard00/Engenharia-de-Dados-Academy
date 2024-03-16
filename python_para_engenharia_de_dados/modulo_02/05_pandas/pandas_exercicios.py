from tracemalloc import start
import pandas as pd
import numpy as np

np.random.seed(0)  # Para garantir que os resultados sejam reproduzíveis.

# 1. Crie um data frame pandas com 1000 amostras em cada uma das seguintes colunas:
# 1. Idade: números inteiros aleatórios ente 0 e 100 (inclusos).
age = np.random.randint(0, 101, 1000)

# 2. Data: data aleatórias entre 01/01/2000 até 31/01/2000.
start_date = "2000-01-01"
random_dates = np.random.randint(1, 32, 1000)
dates = pd.to_datetime(random_dates, origin=start_date, unit="D").date

# 3. Nota: Números decimais entre 0 e 1000.
grades = np.random.uniform(0, 1000.01, 1000).round(2)

# 4. Sexo: Valores aleatórios de M e F.
sex = np.random.choice(["M", "F"], 1000)

# 5. Estado: Valores aleatórios entre os estados do Brasil.
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
    {"age": age, "date": dates, "grade": grades, "sex": sex, "state": states}
)

# max_grade = df["grade"].idxmax()
# print(df.iloc[max_grade])

# 2. Utilizando pandas, realizze as seguintes alterações no dataset: (semente 0)
# 1. Transforme 20% das notas em valorres nulos, simulando alkunos que não compareceram à prova,.
# 2. Preencha as notas nulas com valor 0, simulando uma atribuição automática do sistema.
# 3. Remova alunos com idades infferiores a 18 anos e superiores a 80, simulando uma ffiltragem
#       automática do sistema para alunos com idades incosistentes.
# 4. Crie um novo campo de aprovado para os alunos restantes que obtiveram nota igual ou superior
#       a 600. Simulando uma correção automática.
# 5. Crie um campo novo indicando o dia da semana para todas as datas.

# 3. Gere um relatório com os seguintes tópicos:
# 1. Tabela cruzada de participantes de cada sexo por estado.
# 2. Gráffico de pizza da quantidade de aprovados por sexo e um de barras com a quantidade de aprovados por estado
# 3. Gráfico de pontos de uma nota por idade, colorindo por sexo.
#       1. Gráfico de barras com a participação por dia da semana e por dia do mês.add()
#       2. Gráfico de pontos das notas por dia da semana.

# 4. Salve um arquivo csv com as notas dos 100 melhores alunos ordenados da melhor nota para a pior.
