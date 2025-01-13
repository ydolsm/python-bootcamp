def get_number_items():
    """Ask number for a valid positive number and return (int)"""

def get_item_prices(repeat):
    """Ask the user for item prices repeat times and return total (int)"""

def display(total_price):
    """Print a message about the total_price"""

def main():
    number_of_items = get_number_items()
    total = get_item_prices(repeat=number_of_items)
    display(total)

main()