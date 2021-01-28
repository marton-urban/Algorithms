one_digit_wrong1 = input("One digit is right but in the wrong place (example input: 147): ")
one_digit_right = input("One digit is right and in its place (example input: 189): ")
two_correct = input("Two digits are correct but both are in the wrong place (example input: 964): ")
wrong_digits = input("All digit are wrong (example input: 523): ")
one_digit_wrong2 = input("One digit is right but in the wrong place (example input: 286): ")
one_digit_wrong = [one_digit_wrong1, one_digit_wrong2, two_correct]

one_possible_comb = [0, 1, 2]
possible_combs = []

"""Rule 4 and initialization for rule 2:
Remove the digits of rule 2 as well, because they will be referenced directly using 
one_digit_right[0], one_digit_right[1], and one_digit_right[2] in the next loop."""
possible_digits_left = [digit for digit in range(10) if str(digit) not in wrong_digits and
                        str(digit) not in one_digit_right]

"""Add all possible combinations by rule 2.
Direct reference to the digits, all other decimal places will be filled from possible_digits_left."""
for place in range(3):
    one_possible_comb[place] = int(one_digit_right[place])
    pos = [0, 1, 2]
    pos.remove(place)
    for first in possible_digits_left:
        for second in filter(lambda second: second != first, possible_digits_left):
            one_possible_comb[pos[0]] = first
            one_possible_comb[pos[1]] = second
            possible_combs.append(list(one_possible_comb))
# +3*12 possibilities = 36 left

"""Remove all possible combinations by rules 1, 3 and 5.
"two digits are correct but both are in the wrong place" =
"one digit is right but in the wrong place", the 5 possible permutations are identical"""
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

print("\nHere are the possible combinations: ", end="")
for combination in possible_combs:
    print(''.join(map(str, combination)), end=" ")
