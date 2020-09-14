'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # define the string we're looking for
    word_contains = "th"

    # base case: if it's less than 2 we know it can't have 'th in it.
    if len(word) < 2:
        return False
    # recursion case:  
    if word[0:2] == word_contains:
        # if the first 2 indexes = the string, return 1 and then run it again starting
        # from 2 etc etc
        return 1 + count_th(word[2:])
    else:
        # after recursion return:
        return count_th(word[1:])


# print(count_th("abcabcabcabcthasdasdthththththththasfrgtjndfghdfgzs"))


# UNDERSTAND

# (word) will be given to us by the test.
# we are checking for number of occurances of 'th' (case sebsitive)
# NO LOOPS
# recursion.

# PLAN

# we need a variable for number of th's.
# we need a base case.
# recursive case that keeps adding to increment and moving up one index

# EXECUTE
# see above

# REFLECT
# I think this is about as simple as it can get for a recursive method of doing this
# in a real world project, I'd probably wanna just use .count, built in python method
# could do:
# th_count = word.count(word_contains) and return that number.
