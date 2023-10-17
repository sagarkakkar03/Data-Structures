import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, capacity, dish, cost):
        # print(capacity)
        # print(dish)
        # print(cost)
        ans = 0
        cap = max(capacity)
        n = len(cost)
        z = sorted([i for i in zip(dish, cost)])
        price = [[float('inf') for i in range(cap+1)] for j in range(n+1)]
        for i in range(n+1):
            price[i][0] = 0
        for row in range(1, n+1):
            for col in range(1, cap+1):
                price[row][col] = price[row-1][col]
                if col - z[row-1][0] >=0:
                    price[row][col] = min(price[row-1][col-z[row-1][0]] + z[row-1][1], price[row][col-z[row-1][0]] + z[row-1][1], price[row][col])
        ans = 0
        for cap in capacity:
            ans += price[-1][cap]
        return ans
