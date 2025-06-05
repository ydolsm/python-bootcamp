from openpyxl import load_workbook

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

sheet["B1"].number_format = "#,##0"
workbook.save("sample.xlsx")
