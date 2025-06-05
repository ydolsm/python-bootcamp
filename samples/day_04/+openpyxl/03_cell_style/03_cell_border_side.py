from openpyxl import load_workbook
from openpyxl.styles import Side, Border

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

ss = Side(style="thin", color="000000")

for (cell,) in sheet["A3:A7"]:
    cell.border = Border(left=ss, right=ss, top=ss, bottom=ss)

workbook.save("sample.xlsx")
