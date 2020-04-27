# asked to print a given string according to odd then even indexes respectively
def alternating_split(string):
	arr = [i for i in string]
	out = ""
	for i in range(len(arr)):
		if i % 2 == 1:
			out += arr[i]
	for i in range(len(arr)):
		if i % 2 == 0:
			out += arr[i]
	return out
	
print(alternating_split("This is a test"))