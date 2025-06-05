from openpyxl import load_workbook

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]
sheet.delete_rows(1)
sheet.delete_rows(1)

workbook.save("sample.xlsx")
