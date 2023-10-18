class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @return a list of integers
	def solve(self, A, B, C, D):
		i = 0
		j = 0
		k = 0
		arr = [1]
		this = set()
		while len(arr) <= D:
			if arr[j]*B >= arr[i]*A <= arr[k]*C:
				if arr[i]*A not in this:
					arr.append(arr[i]*A)
					this.add(arr[i]*A)
				i += 1
			elif arr[i]*A >= arr[j]*B <= arr[k]*C:
				if arr[j]*B not in this:
					this.add(arr[j]*B)
					arr.append(arr[j]*B)
				j += 1
			else:
				if arr[k]*C not in this:
					this.add(arr[k]*C)
					arr.append(arr[k]*C)
				k += 1
		return arr[1:]
