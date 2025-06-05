from openpyxl import Workbook


workbook = Workbook()
sheet = workbook["Sheet"]
workbook.create_sheet("Additional")

workbook.save("sample.xlsx")
