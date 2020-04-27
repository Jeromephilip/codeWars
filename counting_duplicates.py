# If a letter is duplicated, then count it
def duplicate_count(text):
    values = {}
    arr = []
    score = 0
    text = text.lower()
    for char in text: 
        if char in values:
            values[char] += 1
        else:
            values[char] = 1
    for v in values.values():
    	if v > 1:
    		arr.append(v)
    return len(arr)

out = duplicate_count("abcdde")
print(out)

