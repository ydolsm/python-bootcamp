from openpyxl import load_workbook
from openpyxl.styles import Protection 

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]
sheet.protection.sheet = True

for (cell,) in sheet["B2:B7"]:
cell.protection = Protection(locked=False)

workbook.save("secured.xlsx")

