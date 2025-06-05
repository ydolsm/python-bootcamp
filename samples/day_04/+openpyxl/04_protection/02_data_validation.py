from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation

workbook = load_workbook("sample.xlsx")
sheet = workbook["Order"]

options_str = '"Laptop,Monitor,Peripheral"'
dv = DataValidation(type="list", formula1=options_str)

sheet.add_data_validation(dv)
dv.add("A2:A100")
workbook.save("sample.xlsx")
