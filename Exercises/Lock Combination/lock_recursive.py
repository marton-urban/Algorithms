# one_digit_wrong1 = input("One digit is right but in the wrong place (example input: 147): ")
# one_digit_right = input("One digit is right and in its place (example input: 189): ")
# two_correct = input("Two digits are correct but both are in the wrong place (example input: 964): ")
# wrong_digits = input("All digit are wrong (example input: 523): ")
# one_digit_wrong2 = input("One digit is right but in the wrong place (example input: 286): ")
# one_digit_wrong = [one_digit_wrong1, one_digit_wrong2, two_correct]
import time


def current_time(name):
    end = time.time()
    if end - start > 1:
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        print("{:0>2}:{:0>2}:{:05.2f} - {} {} {} {} {} ({})".format(int(hours),
                                                                    int(minutes),
                                                                    seconds,
                                                                    one_digit_wrong1,
                                                                    one_digit_right,
                                                                    two_correct,
                                                                    wrong_digits,
                                                                    one_digit_wrong2,
                                                                    name))


def not_allowed(digit_number, number_of_occ, time_it):
    digit_number_rem = digit_number % 3
    if digit_number_rem == 1:
        if digit_number == 1:
            occurences.clear()
        if occurences.count(globals()[f'digit{digit_number}']) == number_of_occ:
            return True
    elif digit_number_rem == 2:
        if globals()[f'digit{digit_number}'] == globals()[f'digit{digit_number - 1}'] or occurences.count(
                globals()[f'digit{digit_number}']) == 2:
            return True
    elif digit_number_rem == 0:
        if globals()[f'digit{digit_number}'] == globals()[f'digit{digit_number - 1}'] or globals()[
            f'digit{digit_number}'] == globals()[f'digit{digit_number - 2}'] or occurences.count(
                globals()[f'digit{digit_number}']) == 2:
            return True
    occurences.append(globals()[f'digit{digit_number}'])
    if time_it:
        current_time(f"Digit{digit_number}")


start = time.time()
occurences = []
for digit1 in range(1, 10):
    if not_allowed(1, 2, False):
        continue
    for digit2 in range(1, 10):
        if not_allowed(2, 2, False):
            continue
        for digit3 in range(1, 10):
            if not_allowed(3, 2, False):
                continue
            one_digit_wrong1 = f"{digit1}{digit2}{digit3}"
            for digit4 in range(1, 10):
                if not_allowed(4, 2, False):
                    continue
                for digit5 in range(1, 10):
                    if not_allowed(5, 2, False):
                        continue
                    for digit6 in range(1, 10):
                        if not_allowed(6, 2, False):
                            continue
                        one_digit_right = f"{digit4}{digit5}{digit6}"
                        for digit7 in range(1, 10):
                            if not_allowed(7, 2, False):
                                continue
                            for digit8 in range(1, 10):
                                if not_allowed(8, 2, False):
                                    continue
                                for digit9 in range(1, 10):
                                    if not_allowed(9, 2, False):
                                        continue
                                    two_correct = f"{digit7}{digit8}{digit9}"
                                    for digit10 in range(1, 10):
                                        if not_allowed(10, 2, False):
                                            continue
                                        for digit11 in range(1, 10):
                                            if not_allowed(11, 2, False):
                                                continue
                                            for digit12 in range(1, 10):
                                                if not_allowed(12, 2, False):
                                                    continue
                                                wrong_digits = f"{digit10}{digit11}{digit12}"
                                                for digit13 in range(1, 10):
                                                    if not_allowed(13, 2, False):
                                                        continue
                                                    for digit14 in range(1, 10):
                                                        if not_allowed(14, 2, False):
                                                            continue
                                                        for digit15 in range(1, 10):
                                                            if not_allowed(15, 2, False):
                                                                continue
                                                            one_digit_wrong2 = f"{digit13}{digit14}{digit15}"
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
                                                                print("\nHere are the possible combinations for "
                                                                      f"{one_digit_wrong1} {one_digit_right} "
                                                                      f"{two_correct} {wrong_digits} "
                                                                      f"{one_digit_wrong2}: ",
                                                                      end="")
                                                                for combination in possible_combs:
                                                                    print(''.join(map(str, combination)), end=" ")

                                                                end = time.time()
                                                                if end - start >= 0:
                                                                    hours, rem = divmod(end - start, 3600)
                                                                    minutes, seconds = divmod(rem, 60)
                                                                    print("\t({:0>2}:{:0>2}:{:05.2f})".format(
                                                                        int(hours),
                                                                        int(minutes),
                                                                        seconds, ))
