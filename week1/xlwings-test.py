import xlwings as xw

wk = xw.books.open(r"C:\Users\miwan\Desktop\Everest Times.xlsx")
# sheet = wk.sheets["Sheet1"]
sheet = wk.sheets[0]
rg = sheet.range("A1:G20")
print(rg.value)

