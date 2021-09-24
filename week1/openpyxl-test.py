import openpyxl

book = openpyxl.load_workbook(r"C:\Users\miwan\Desktop\Everest Times.xlsx")

sheet = book["Sheet1"]

# print(sheet["A8"])
print(sheet["C6"].value)
print(sheet.cell(3,4).value)

