# You are asked to find the next squared number depending on the given squared number. Example, 
# if input is 144, then the next would be 169. If the number given is not a perfect square, then return -1. 

import math

def nextsquareroot(inp):
	initial = math.sqrt(inp)
	x = initial - math.floor(initial)
	if x == 0:
		out = (initial+1)*(initial+1)
		return out
	else:
		return (-1)

out = nextsquareroot(144)
print(out)

