from itertools import combinations
import random

class Task:
    def __init__(self, name, start_time, end_time, duration):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

#define tasks
t1 = Task('Clean house', 8, 18, 1)
t2 = Task('Cooking', 11, 12, 1)
t3 = Task('Study Math', 8, 22, 4)
t4 = Task('Study Geo', 8, 22, 4)

tasks = [t1, t2, t3, t4]

start = {}
end = {}

# Define domains
for t in tasks:
    start[t] = 0
    end[t] = 1

# Define constraints
def is_valid():
    for t in tasks:
        end[t] = start[t] + t.duration
        if end[t] > t.end_time:
            return False
    for t1, t2 in combinations(tasks, 2):
        if end[t1] > start[t2] and end[t2] > start[t1]:
            return False
    return True

# Find a solution
found_solution = False
while not found_solution:
    # Generate a random assignment
    for t in tasks:
        start[t] = random.randint(t.start_time, t.end_time-1)
    # Check if the assignment is valid
    if is_valid():
        found_solution = True

# Print solution
for t in tasks:
    print('%s starts at %d and ends at %d' % (t.name, start[t], end[t]))