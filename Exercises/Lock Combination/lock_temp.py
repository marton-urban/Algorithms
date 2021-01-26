possible_digits_left = [0, 4, 6, 7]

for first in possible_digits_left:
    for second in filter(lambda second: second != first, possible_digits_left):
        print(f"{first} {second}")

one_possible_comb = [0,1,2]
one_possible_comb[1] = 'második kéne hogy legyen'
one_possible_comb[0] = 'első'

print(one_possible_comb)

for place in range(3):
    pos = [0, 1, 2]
    pos.remove(place)
    print(pos)