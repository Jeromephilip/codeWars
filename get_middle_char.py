def middle(string):
	arr = []
	count = 0
	for i in string:
		arr.append(i)
# Should be using len() instead of loop. Jerome?? 
	for j in arr:
		count+=1 
	out = count-1
	divide = int(out/2)
	if count % 2 == 0:
		index_one = int((out/2) + 1.5)
		index_two = int((out/2) - 0.5)	
		final = arr[index_two:index_one]
		final_out = ('').join(final)
		return final_out
	return arr[divide]



print(middle("testss"))
