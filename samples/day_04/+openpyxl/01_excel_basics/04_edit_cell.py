from openpyxl import Workbook


workbook = Workbook()
sheet = workbook["Sheet"]
workbook.create_sheet("Additional")
sheet["A1"] = "Hello"
workbook.save("sample.xlsx")
