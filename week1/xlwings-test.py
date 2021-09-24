import xlwings as xw
import pandas as pd

# xw.App().visible = False         #this should be used if you want to not have the excel file open

wk = xw.books.open(r'C:\Users\miwan\Desktop\Everest Times.xlsx')
# sheet = wk.sheets["Sheet1"]
sheet = wk.sheets[0]
rg = sheet.range("A1:G20")
print(rg.value)


df = sheet.range("A1:G20").options(pd.DataFrame).value     #creates dataframe


xw.view(df)                 #opens a new workbook in Excel to view dataframe result

# xw.close