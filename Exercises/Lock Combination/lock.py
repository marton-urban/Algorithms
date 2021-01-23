one_digit_wrong1 = str(input("One digit is right but in the wrong place (example input: 147): "))
one_digit_right = str(input("One digit is right and in its place (example input: 189): "))
two_correct = str(input("Two digits are correct but both are in the wrong place (example input: 964): "))
wrong_digits = str(input("All digit are wrong (example input: 523): "))
one_digit_wrong2 = str(input("One digit is right but in the wrong place (example input: 268): "))
one_digit_wrong = [one_digit_wrong1, one_digit_wrong2, two_correct]

all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
one_possible_comb = []
possible_combs = []

"""Rule 4 and initialization for rule 2:
Remove the digits of rule 2 as well, because they will be referenced directly using 
one_digit_right[0], one_digit_right[1], and one_digit_right[2] in the next loop."""
possible_digits_left = [digit for digit in range(10) if
                        str(digit) != one_digit_right[0] and
                        str(digit) != one_digit_right[1] and
                        str(digit) != one_digit_right[2] and
                        str(digit) != wrong_digits[0] and
                        str(digit) != wrong_digits[1] and
                        str(digit) != wrong_digits[2]]

"""Rule 2:
Direct reference to the digits, all other decimal places will be filled from possible_digits_left."""
for place in range(3):
    for digit in possible_digits_left:

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
# 36 left

"""For rules 1, 3 and 5.
"two digits are correct but both are in the wrong place" =
"one digit is right but in the wrong place", the 5 possible permutations are identical)"""
for rule in one_digit_wrong:
    for place in range(3):
        [possible_combs.remove(possible_combination) for possible_combination in possible_combs.copy()
         if int(rule[place]) == possible_combination[place] or
         (int(rule[0]) not in possible_combination and
          int(rule[1]) not in possible_combination and
          int(rule[2]) not in possible_combination)
         ]
        place += 1
# 1 left

for combination in possible_combs:
    print(f"Here are the possible combinations when all rules are regarded: {''.join(map(str, combination))} ")
