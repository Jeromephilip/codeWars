# Question asks to print the highest highest alphabetical summmed word in a given string
def high(string):
	for k in string:
		k.lower()
	words = [i for i in string.split(" ")]
	alphabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
	'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
	total = 0
	word = None
	for i in words:
		number = 0
		for j in i:
			number += int(alphabet[j])
		if number > total:
			total = number
			word = i
	return word

print(high('man i need a taxi up to ubud'))