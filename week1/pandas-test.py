import pandas as pd

df = pd.read_excel(r"C:\Users\miwan\Desktop\Everest Times.xlsx",engine="openpyxl")

results = df.iloc[:6,2:4]


print(results)