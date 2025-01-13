def create_deck() -> list[str]:
	"""Return a list of 52 strings containing a standard deck"""

def draw_top(deck: list[str], count: int=1)-> list[str]:
	"""Remove count return count cards from the start from deck"""

def draw_bottom(deck: list[str], count: int=1) -> list[str]:
	"""Remove and return count cards from the end of the deck"""

def draw_random(deck: list[str], count: int=1) -> list[str]:
	"""Remove and return count random cards from the deck"""

def show(deck):
	"""Print all cards in deck"""

# Use this to test:

deck = create_deck()
show(deck)

top_five_cards = draw_top(deck, count=5)
show(top_five_cards)

bottom_five_cards = draw_bottom(deck, count=5)
show(bottom_five_cards)

random_five_cards = draw_random(deck, count=5)
show(random_five_cards)