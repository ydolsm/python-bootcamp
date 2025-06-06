total_cost = 0
item_count = int(input("Enter number of items: "))

for item in range(item_count):
    item_price = int(input(f"Item Price: "))
    item_packs = int(input(f"Item Packs: "))
    total_cost += item_price * item_packs
print (total_cost)

#print ("Grand Total:", grand_total)

