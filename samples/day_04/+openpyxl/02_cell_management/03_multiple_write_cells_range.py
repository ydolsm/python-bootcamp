from openpyxl import load_workbook


workbook = load_workbook("sample.xlsx")
sheet = workbook["Additional"]

tickets = {"HR": 30, "Legal": 23, "Sales": 34, "Admin": 13}

ticket_and_cells = zip(tickets.items(), sheet["A3:B6"])

for (group, count), (group_cell, count_cell) in ticket_and_cells:
    group_cell.value = group
    count_cell.value = count

workbook.save("sample.xlsx")
