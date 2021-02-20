import time

start_time = time.time()


def count_prize_strings(days):
    """
    Given the number of school days that have passed, calculate the number of possible "prize strings": strings with
    no more than one L and that do not have three consecutive As.
    """

    # We distinguish 6 types of prize string
    # 0: a string with no Ls and no As
    # 1: a string with no L and 1 A
    # 2: a string with no L and 2 As
    # 3: a string with 1 L and no As
    # 4: a string with 1 L and 1 A
    # 5: a string with 1 L and 2 As

    # Iterating on the base case of these permutations, we see what happens to every eligible string when we add
    # on another day of attendance (A,O, or L) and calculate the count of possible prize strings in each category for
    # the next day. i.e.,

    # type 0 + A = type 1
    # type 1 + A = type 2
    # type 2 + A = INVALID
    # type 3 + A = type 4
    # type 4 + A = type 5
    # type 5 + A = INVALID
    #
    # type 0 + O = type 0
    # type 1 + O = type 0
    # type 2 + O = type 0
    # type 3 + O = type 3
    # type 4 + O = type 3
    # type 5 + O = type 3
    #
    # type 0 + L = type 3
    # type 1 + L = type 3
    # type 2 + L = type 3
    # type 3 + L = INVALID
    # type 4 + L = INVALID
    # type 5 + L = INVALID

    # create 2D array where
    # rows -> # of one of the prize string types over every day
    # columns -> # of each string type on a given day
    prize_strings = [[0] * 6 for i in range(days)]

    # categorize base case strings (A,O,L) into the 6 types:
    prize_strings[0] = [1, 1, 0, 1, 0, 0]

    for i in range(days - 1):
        # calculate of each prize string type on the i+1th day by iterating according to the patterns shown in
        # comments above
        prize_strings[i + 1][0] = prize_strings[i][0] + prize_strings[i][1] + prize_strings[i][2]
        prize_strings[i + 1][1] = prize_strings[i][0]
        prize_strings[i + 1][2] = prize_strings[i][1]
        prize_strings[i + 1][3] = prize_strings[i][0] + prize_strings[i][1] + prize_strings[i][2] + prize_strings[i][
            3] + prize_strings[i][4] + prize_strings[i][5]
        prize_strings[i + 1][4] = prize_strings[i][3]
        prize_strings[i + 1][5] = prize_strings[i][4]

    return sum(prize_strings[-1])

day = 30

# call function for solution to problem #2
total_prize_strings = count_prize_strings(day)

# print solution
print("There are " + str(total_prize_strings) + " prize strings on day " + str(day))
# use current time and start time to calculate execution time and print
print("Execution time: %s seconds " % (time.time() - start_time))
