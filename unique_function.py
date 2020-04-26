# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
# any elements with the same value next to each other and preserving the original order of elements.

def unique(arr):
	for i in range(0, len(arr)-1, 1):
		if arr[i] == arr[i-1]:
			arr.remove(arr[i])
	return arr

out = unique([1, 1, 2])
print(out)