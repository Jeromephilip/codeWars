# You are asked to find the a narcisstic number. The sum of the cubes of each digit of a given number should equal the given
# number
def narcissistic(num):
	num = str(num)
	length = len(num)
	arr = []
	for i in num:
		arr.append(int(i)**length)
	if sum(arr) == int(num):
		return True
	return False


out = narcissistic(7)
print(out)
