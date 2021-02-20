# get start time
import time

start_time = time.time()


def coin_combinations(coins, start_index, end_index, coins_left_to_200):
    """
    Given an array of coin values, its starting index, its final index, and a total value,
    find the number of coin combinations that sum to the given total value
    """
    # base case for recursion
    if coins_left_to_200 == 0:
        return 1

    # initialize solution counter
    result = 0

    # if 1st coin type <= total value, subtract one of the first type from the constant value as many times as
    # possible, then subtract the second as many times as possible from the remainder, and so on

    # when our remainder is 0, we have found a solution and increment the solution counter
    for i in range(start_index, end_index + 1):
        if coins[i] <= coins_left_to_200:
            result += coin_combinations(coins, i, end_index, coins_left_to_200 - coins[i])
    return result


# set variables for 2 pound, eight coin problem
british_coins = [200, 100, 50, 20, 10, 5, 2, 1]
start = 0
end = len(british_coins) - 1

# call function for solution to problem #1
combinations = coin_combinations(british_coins, start, end, 200)

# print solution
print("There are " + str(combinations) + " unique combinations.")
# use current time and start time to calculate execution time and print
print("Execution time: %s seconds " % (time.time() - start_time))
