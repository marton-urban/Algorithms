# one_digit_wrong1 = input("One digit is right but in the wrong place (example input: 147): ")
# one_digit_right = input("One digit is right and in its place (example input: 189): ")
# two_correct = input("Two digits are correct but both are in the wrong place (example input: 964): ")
# wrong_digits = input("All digit are wrong (example input: 523): ")
# one_digit_wrong2 = input("One digit is right but in the wrong place (example input: 286): ")
# one_digit_wrong = [one_digit_wrong1, one_digit_wrong2, two_correct]

import time

start = time.time()


def current_time(digit, name):
        if digit > 0 and digit < 2:
            end = time.time()
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


for digit01 in range(10):
    for digit02 in range(10):
        for digit03 in range(10):
            one_digit_wrong1 = f"{digit01}{digit02}{digit03}"
            for digit04 in range(10):
                for digit05 in range(10):
                    for digit06 in range(10):
                        one_digit_right = f"{digit04}{digit05}{digit06}"
                        for digit07 in range(10):
                            for digit08 in range(10):
                                current_time(digit08, 'Digit08')
                                for digit09 in range(10):
                                    current_time(digit09, 'Digit09')
                                    two_correct = f"{digit07}{digit08}{digit09}"
                                    for digit10 in range(10):
                                        current_time(digit10, 'Digit10')
                                        for digit11 in range(10):
                                            for digit12 in range(10):
                                                wrong_digits = f"{digit10}{digit11}{digit12}"
                                                for digit13 in range(10):
                                                    for digit14 in range(10):
                                                        for digit15 in range(10):
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
                                                            possible_digits_left = [str(digit) for digit in range(10) if
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

                                                            if possible_combs:
                                                                print("\nHere are the possible combinations for : "
                                                                      f"{one_digit_wrong1} {one_digit_right} "
                                                                      f"{two_correct} {wrong_digits} "
                                                                      f"{one_digit_wrong2}",
                                                                      end="")
                                                                for combination in possible_combs:
                                                                    print(''.join(map(str, combination)), end=" ")
