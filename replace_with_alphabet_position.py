# Asked to replace all letters in a quote with its position in the alphabet. So 'The' as input would be '20, 8, 5'
# as output

def alphabet_position(text):
	alphabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
	'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
	initial = text.lower()
	arr = []
	final = ""
	for char in initial:
		if char in alphabet:
			arr.append(alphabet[char])
	for num in arr:
		final = final + " " + num
	out = final.strip()
	return out


out = alphabet_position("Jiya")
print(out)

