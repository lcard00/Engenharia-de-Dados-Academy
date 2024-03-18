import requests
import pandas as pd

base_url = "https://covid19-brazil-api.now.sh/api/report/v1"
module = "countries"
url = f"{base_url}/{module}"

response = requests.get(url)
result = response.json()

df = pd.DataFrame(result["data"])

# print(df.info())

del df["cases"]
del df["recovered"]
df.drop(columns=["updated_at"], inplace=True)

# print(df.duplicated().any())

df.columns = [
    "pais",
    "total_confirmados",
    "total_obitos"
]

# print(df)

df.to_csv("files/cleaned_covid19_world.csv", index=False)


