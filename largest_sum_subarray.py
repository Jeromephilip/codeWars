# You are asked to find the largest sum subarray in an inputed array. 
# Instead of brute forcing it, we can use Kadane's Algorithm
# Self-Note: It is not asking for the index of arrays, it is asking for the largest sum of contigious numbers in the array

from sys import maxsize
def maxSubArraySum(a):
	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0
	for i in range(0, len(a)):
		max_ending_here += a[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i
		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1
	return max_so_far

print(maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]))