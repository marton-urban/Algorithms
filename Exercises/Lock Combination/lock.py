wrong_digits = 523
one_digit_right = 189

all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
wrong_digits = [int(digit) for digit in str(wrong_digits)]
one_digit_right = [int(digit) for digit in str(one_digit_right)]

# possible_digits = [digit for digit in all_digits if digit not in wrong_digits]
possible_combination = []
possible_digits_left = [digit for digit in range(10) if
                        digit != one_digit_right[0] and
                        digit != one_digit_right[1] and
                        digit != one_digit_right[2] and
                        digit != wrong_digits[0] and
                        digit != wrong_digits[1] and
                        digit != wrong_digits[2]]
