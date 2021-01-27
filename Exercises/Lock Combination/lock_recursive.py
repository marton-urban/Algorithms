# one_digit_wrong1 = input("One digit is right but in the wrong place (example input: 147): ")
# one_digit_right = input("One digit is right and in its place (example input: 189): ")
# two_correct = input("Two digits are correct but both are in the wrong place (example input: 964): ")
# wrong_digits = input("All digit are wrong (example input: 523): ")
# one_digit_wrong2 = input("One digit is right but in the wrong place (example input: 286): ")
# one_digit_wrong = [one_digit_wrong1, one_digit_wrong2, two_correct]
import time


def current_time():
    end = time.time()
    if end - start >= 0:
        hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("\t{:0>2}:{:0>2}:{:05.2f} - ".format(int(hours), int(minutes), seconds), end="")


def not_allowed(digit, number_of_occ):
    digit_number = all_digits['digit_number']
    digit_number_rem = digit_number % 3
    if digit_number_rem == 1:
        if digit_number == 1:
            occurences.clear()
        if occurences.count(digit) == number_of_occ:
            return True
        all_digits[str(digit_number)] = digit
    elif digit_number_rem == 2:
        if digit == all_digits[str(digit_number - 1)] or occurences.count(digit) == number_of_occ:
            return True
        all_digits[str(digit_number)] = digit
    elif digit_number_rem == 0:
        if digit == all_digits[str(digit_number - 1)] or digit == all_digits[str(digit_number - 2)] or occurences.count(
                digit) == number_of_occ:
            return True
        all_digits[str(digit_number)] = digit
        if digit_number == 3:
            all_digits['one_digit_wrong1'] = f"{all_digits['1']}{all_digits['2']}{all_digits['3']}"
        elif digit_number == 6:
            all_digits['one_digit_right'] = f"{all_digits['4']}{all_digits['5']}{all_digits['6']}"
        elif digit_number == 9:
            all_digits['two_correct'] = f"{all_digits['7']}{all_digits['8']}{all_digits['9']}"
        elif digit_number == 12:
            all_digits['wrong_digits'] = f"{all_digits['10']}{all_digits['11']}{all_digits['12']}"
        elif digit_number == 15:
            all_digits['one_digit_wrong2'] = f"{all_digits['13']}{all_digits['14']}{all_digits['15']}"
    occurences.append(digit)


def generate_all_digits(number_of_digits, number_of_occ, print_or_sum):
    all_digits['digit_number'] += 1
    if number_of_digits > 0:
        for digit in range(1, 10):
            if not_allowed(digit, number_of_occ):
                continue
            generate_all_digits(number_of_digits - 1, number_of_occ, print_or_sum)
    all_digits['digit_number'] -= 1
    occurences.pop()
    if all_digits['digit_number'] == 15:
        check_numbers_against_rules(print_or_sum)


def check_numbers_against_rules(print_or_sum):
    one_digit_wrong1 = all_digits['one_digit_wrong1']
    one_digit_right = all_digits['one_digit_right']
    two_correct = all_digits['two_correct']
    wrong_digits = all_digits['wrong_digits']
    one_digit_wrong2 = all_digits['one_digit_wrong2']

    one_digit_wrong = [one_digit_wrong1, one_digit_wrong2,
                       two_correct]

    one_possible_comb = ['0', '1', '2']
    possible_combs = []

    """Rule 4 and initialization for rule 2:
    Remove the digits of rule 2 as well,
    because they will be referenced directly using 
    one_digit_right[0], one_digit_right[1], 
    and one_digit_right[2] in the next loop."""
    possible_digits_left = [str(digit) for digit in range(1, 10)
                            if
                            str(digit) not in wrong_digits and
                            str(digit) not in one_digit_right]

    """Adds all possible combinations by rule 2.
    Direct reference to the digits, all other decimal places
    will be filled from possible_digits_left."""
    for place in range(3):
        one_possible_comb[place] = str(one_digit_right[place])
    pos = [0, 1, 2]
    pos.remove(place)
    for first in possible_digits_left:
        for second in filter(lambda second: second != first,
                             possible_digits_left):
            one_possible_comb[pos[0]] = str(first)
            one_possible_comb[pos[1]] = str(second)
            possible_combs.append(list(one_possible_comb))
    # +3*12 possibilities = 36 left

    """Removes all possible combinations by rules 1, 3 and 5.
    "two digits are correct but both are in the wrong place" =
    "one digit is right but in the wrong place",
    the 5 possible permutations are identical)"""
    for rule in one_digit_wrong:
        for place in range(3):
            [possible_combs.remove(possible_combination) for
             possible_combination in possible_combs.copy()
             if rule[place] == possible_combination[place] or
             (rule[0] not in possible_combination and
              rule[1] not in possible_combination and
              rule[2] not in possible_combination)
             ]
            place += 1
    # 1 left

    if len(possible_combs) == 1:
        if print_or_sum == 'sum':
            global sum_of_all, another_thousand
            sum_of_all += 1
            if sum_of_all >= another_thousand:
                another_thousand += 10000000
                current_time()
                print(
                    f"One-solution puzzles so far: {int(sum_of_all / 10000000)} million"
                    f" - last: {all_digits['one_digit_wrong1']} "
                    f"{all_digits['one_digit_right']} "
                    f"{all_digits['two_correct']} "
                    f"{all_digits['wrong_digits']} "
                    f"{all_digits['one_digit_wrong2']} ({''.join(map(str, possible_combs[0]))})")
        else:
            current_time()
            print("Here are the possible combinations for "
                  f"{one_digit_wrong1} {one_digit_right} "
                  f"{two_correct} {wrong_digits} "
                  f"{one_digit_wrong2}: ",
                  end="")
            for combination in possible_combs:
                print(''.join(map(str, combination)))


start = time.time()
occurences = []
all_digits = {'digit_number': 0}
sum_of_all = 0
another_thousand = 10000000

generate_all_digits(15, 2, 'sum')
