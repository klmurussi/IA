import random

def monty_hall(change_choice):
    winning_door = random.randint(1,3)
    player_choice = random.randint(1,3)
    if player_choice == winning_door:
        revealed_door = random.choice([door for door in [1,2,3] if door != player_choice])
    else:
        revealed_door = [door for door in [1,2,3] if door != player_choice and door != winning_door][0]
    if change_choice:
        player_choice = [door for door in [1,2,3] if door != player_choice and door != revealed_door][0]
    return player_choice == winning_door

def monty_hall_simulation(change_choice, num_trials):
    win_count = 0
    for i in range(num_trials):
        win = monty_hall(change_choice)
        if win:
            win_count += 1
    return win_count/num_trials

num_trials = 10000
print("Probability of winning if you stick with your initial choice:", monty_hall_simulation(False, num_trials))
print("Probability of winning if you change your initial choice:", monty_hall_simulation(True, num_trials))
