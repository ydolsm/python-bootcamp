from openpyxl import Workbook


workbook = Workbook()
sheet = workbook["Sheet"]


workbook.save("sample.xlsx")
