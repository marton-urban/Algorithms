l = [[1, 0, 4], [1, 0, 6], [1, 0, 7], [1, 4, 0], [1, 4, 6], [1, 4, 7], [1, 6, 0], [1, 6, 4], [1, 6, 7], [1, 7, 0],
     [1, 7, 4], [1, 7, 6], [0, 8, 4], [0, 8, 6], [0, 8, 7], [4, 8, 0], [4, 8, 6], [4, 8, 7], [6, 8, 0], [6, 8, 4],
     [6, 8, 7], [7, 8, 0], [7, 8, 4], [7, 8, 6], [0, 4, 9], [0, 6, 9], [0, 7, 9], [4, 0, 9], [4, 6, 9], [4, 7, 9],
     [6, 0, 9], [6, 4, 9], [6, 7, 9], [7, 0, 9], [7, 4, 9], [7, 6, 9]]

one_digit_wrong1 = str(147)

for place in range(3):
     [ l.remove(possible_comb) for possible_comb in l.copy() if int(one_digit_wrong1[place]) in possible_comb and int(one_digit_wrong1[place]) == possible_comb[place] ]
     place += 1

print(l)
print(len(l))

