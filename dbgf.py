# max weight 30
# jewel 5($50), 10($60), 20($140)

def steal_jewals (max_weight, weight, value) :
	n = len(value)
	ans = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]

	for i in range(n+1) :
		for w in range(max_weight+1) :
			if i == 0 or w == 0	:
				ans[i][w] = 0
			elif weight[i-1] <= w :
				ans[i][w] = max(value[i-1] + ans[i-1][w - weight[i-1]], ans[i-1][w])
			else :
				ans[i][w] = ans[i-1][w]

	return ans[n][max_weight]

value = [50, 60, 140]
weight = [5, 10, 20]
max_weight = 30

print("The best score is :",steal_jewals(max_weight, weight,value))