wrong_digits = str(523)
one_digit_right = str(189)
one_digit_wrong1 = str(147)

all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# possible_digits = [digit for digit in all_digits if digit not in wrong_digits]
possible_combs = []
possible_digits_left = [digit for digit in range(10) if
                        str(digit) != one_digit_right[0] and
                        str(digit) != one_digit_right[1] and
                        str(digit) != one_digit_right[2] and
                        str(digit) != wrong_digits[0] and
                        str(digit) != wrong_digits[1] and
                        str(digit) != wrong_digits[2]]

"""One digit is right and its place (first digit)"""
one_possible_comb = []
one_possible_comb.append(int(one_digit_right[0]))
one_possible_comb.append('will be removed')
for digit in range(len(possible_digits_left)):
    one_possible_comb.pop()
    one_possible_comb.append(possible_digits_left[digit])
    for digit2 in possible_digits_left:
        if digit2 != possible_digits_left[digit]:
            one_possible_comb.append(digit2)
            possible_combs.append(one_possible_comb.copy())
            one_possible_comb.pop()

"""One digit is right and its place (second digit)"""
for digit in possible_digits_left:
    one_possible_comb = []
    one_possible_comb.append(digit)
    one_possible_comb.append(int(one_digit_right[1]))
    for digit2 in possible_digits_left:
        if digit2 != digit:
            one_possible_comb.append(digit2)
            possible_combs.append(one_possible_comb.copy())
            one_possible_comb.pop()

"""One digit is right and its place (third digit)"""
for digit in possible_digits_left:
    one_possible_comb = []
    one_possible_comb.append(digit)
    for digit2 in possible_digits_left:
        if digit2 != digit:
            one_possible_comb.append(digit2)
            one_possible_comb.append(int(one_digit_right[2]))
            possible_combs.append(one_possible_comb.copy())
            one_possible_comb.pop()
            one_possible_comb.pop()
# 36 left

"""One digit is right but in the wrong place"""
for place in range(3):
     [ possible_combs.remove(possible_combination) for possible_combination in possible_combs.copy()
       if int(one_digit_wrong1[place]) in possible_combination and int(one_digit_wrong1[place]) == possible_combination[place] ]
     place += 1
# 18 left

print(len(possible_combs))