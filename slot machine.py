import random

def slot_machine():
    winnings = -1
    symbols = [random.choice(["cherry", "lemon", "apple", "bell", "seven"]) for i in range(3)]
    if len(set(symbols)) == 1:
        winnings += 10
    elif symbols[0] == symbols[1]:
        winnings += 5
    return winnings

def monte_carlo_simulation(num_plays):
    winnings = 0
    for i in range(num_plays):
        winnings += slot_machine()
    return winnings / num_plays

num_plays = 100000
test = 10
for i in range (test):
	#average_winnings = monte_carlo_simulation(num_plays)
    print("Total winnings:", i+1, monte_carlo_simulation(num_plays))