from openpyxl import load_workbook
from openpyxl.styles import Font

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

sheet["A1"].font = Font(name="Arial", size=20)
workbook.save("sample.xlsx")
