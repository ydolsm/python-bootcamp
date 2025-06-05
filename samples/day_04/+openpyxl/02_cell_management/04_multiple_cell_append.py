from openpyxl import load_workbook

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

new_data = ["Tech", 300]
sheet.append(new_data)

workbook.save("sample.xlsx")
