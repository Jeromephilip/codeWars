# You are asked to find the highest and lowest number of a given string of numbers evenly spaced. 
def high_and_low(numbers):
	x = max([int(i) for i in numbers.split(' ')])
	y = min([int(i) for i in numbers.split(' ')])
	return str(x) + ' ' + str(y)

out = high_and_low("1 2 3 4")
print(out)