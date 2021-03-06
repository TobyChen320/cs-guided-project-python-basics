"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""


# def XO(txt:str) -> bool:
#     # set an o and x counter to zero
#     o_counter = 0
#     x_counter = 0
#     # loop over each character in the string
#     for char in txt:
#         # do a check if it contains an "x"
#         if char == "x":
#             # increment the x counter
#             x_counter += 1
#         # do a check if it contains an "X"
#         elif char == "X":
#             # increment the x counter
#             x_counter += 1
#         # do a check if it contains an "o"
#         elif char == "o":
#             # increment the o counter
#             o_counter += 1
#         # do a check if it contains an "O"
#         elif char == "O":
#             # increment the o counter
#             o_counter += 1

#     # check if x counter is equal to o counter
#     if x_counter == o_counter:
#         # return true to the caller
#         return True
#     # otherwise
#     else:
#         # return false to the caller
#         return False

# def XO(txt:str):
#     o_counter = 0
#     x_counter = 0
#     for char in txt:
#         if char is "x" or  char is "X":
#             x_counter += 1
#         elif char is "o" or char is "O":
#             o_counter += 1
#     return x_counter is o_counter

def XO(txt):
    return (txt.lower().count('x') is txt.lower().count('o'))


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
