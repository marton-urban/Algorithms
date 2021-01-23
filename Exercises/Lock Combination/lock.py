wrong_digits = str(523)
one_digit_right = str(189)
one_digit_wrong1 = str(147)
one_digit_wrong2 = str(286)
two_correct = str(964)

all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    [possible_combs.remove(possible_combination) for possible_combination in possible_combs.copy()
     if int(one_digit_wrong1[place]) == possible_combination[place] or
     (int(one_digit_wrong1[0]) not in possible_combination and
      int(one_digit_wrong1[1]) not in possible_combination and
      int(one_digit_wrong1[2]) not in possible_combination)
     ]
    place += 1
# 14 left

"""One digit is right but in the wrong place (second)"""
for place in range(3):
    [possible_combs.remove(possible_combination) for possible_combination in possible_combs.copy()
     if int(one_digit_wrong2[place]) == possible_combination[place] or
     (int(one_digit_wrong2[0]) not in possible_combination and
      int(one_digit_wrong2[1]) not in possible_combination and
      int(one_digit_wrong2[2]) not in possible_combination)
     ]
    place += 1
# 3 left

"""One digit is right but in the wrong place (third)"""
for place in range(3):
    [possible_combs.remove(possible_combination) for possible_combination in possible_combs.copy()
     if int(two_correct[place]) == possible_combination[place] or
     (int(two_correct[0]) not in possible_combination and
      int(two_correct[1]) not in possible_combination and
      int(two_correct[2]) not in possible_combination)
     ]
    place += 1
#  1 left

for combination in possible_combs:
    print(f"Here are the possible combinations when all rules are regarded: {''.join(map(str, combination))} ")
