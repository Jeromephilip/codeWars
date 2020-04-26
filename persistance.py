# asked to return the inputs nmultiplicative persistance, which is the number of times you must multiply the digits in
# num until you reach a single digit. 

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

out = persistence(999)
print(out)