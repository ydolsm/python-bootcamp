from openpyxl import load_workbook

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]
sheet["A1"] = None
sheet["B1"] = None

workbook.save("sample.xlsx")
