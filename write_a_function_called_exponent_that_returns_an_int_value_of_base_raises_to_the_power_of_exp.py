# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.

# Expected output
# Case 1:
# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Case 2:
# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

def calculate(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * calculate(base, exponent - 1)


case_1_base = 2
case_1_exp = 5
result_case_1 = calculate(case_1_base, case_1_exp)


case_2_base = 5
case_2_exp = 4
result_case_2 = calculate(case_2_base, case_2_exp)
