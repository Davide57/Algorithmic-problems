# Given an array, I want to print all the subset in any order you wish

# EXAMPLE:

# [1,2] -> {}, {1,2}, {1}, {2}
# Output:
# > _
# > 1,
# > 2,
# > 1,2,


def printSubset(given_array):
    subset = int[given_array.length]
    explore(given_array, subset, 0)


def explore(given_array, subset, i):
    if i == given_array.length:
        print(subset)
    else:
        # First exploration, without a number
        subset[i] = null
        explore(given_array. subset, i+1)
        #  Second exploration, with the sequel number
        subset[i] = given_array[i]
        explore(given_array, subset, i+1)


# Asked by Facebook