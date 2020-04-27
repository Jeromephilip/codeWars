# gives an array, find a name that has 4 letters
def friend(friend):
	new_friend = []
	for i in friend:
		if len(i) == 4:	
			new_friend.append(i)
	return new_friend

print(friend(["Ryan", "Kieran", "Mark"]))
