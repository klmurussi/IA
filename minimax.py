tree = {
 'A': ('B1', 'B2'),
 'B1': ('C1', 'C2'),
 'B2': ('C3', 'C4'),
 'C1': ('D1', 'D2'),
 'C2': ('D3', 'D4'),
 'C3': ('D5', 'D6'),
 'C4': ('D7', 'D8'),
 'D1': ([], 3),
 'D2': ([], 7),
 'D3': ([], 4),
 'D4': ([], 2),
 'D5': ([], 5),
 'D6': ([], 6),
 'D7': ([], 12),
 'D8': ([], 1)
}


def minimax(depth, node, MaxPlayer):
	if depth == 0:
		print(node + "=" + str(tree[node][1]))
		return int(tree[node][1])

	if MaxPlayer:
		maxValue = float("-inf")
		for neighbour in tree[node]:
			print(neighbour)
			res = minimax(depth - 1, neighbour, False)
			maxValue = max(res, maxValue)
			
		print(node + "=" + str(maxValue))
		return maxValue

	else:
		minValue = float("inf")
		for neighbour in tree[node]:
			print(neighbour)
			res = minimax(depth - 1, neighbour, True)
			minValue = min(res, minValue)
			
		print (node + "=" + str(minValue))
		return minValue


def max(a, b):
	if a >= b:
		return a
	else:
		return b


def min(a, b):
	if a <= b:
		return a
	else:
		return b

minimax(3, 'A', True)