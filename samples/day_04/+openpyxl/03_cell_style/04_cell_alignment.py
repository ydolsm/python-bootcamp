from openpyxl import load_workbook
from openpyxl.styles import Alignment

workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

for (cell,) in sheet["A3:A7"]:
    cell.alignment = Alignment(
        horizontal="center",
        vertical="center",
        wrap_text=True,
        shrink_to_fit=True,
        indent=1,
    )

workbook.save("sample.xlsx")
