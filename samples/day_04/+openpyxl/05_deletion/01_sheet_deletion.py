from openpyxl import load_workbook

workbook = load_workbook("sample.xlsx")
del workbook["Sheet"]

workbook.save("sample.xlsx")
