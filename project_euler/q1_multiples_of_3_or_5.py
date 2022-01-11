#!/usr/bin/env python

"""
Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples_3_5(threshold):
    # Iterate until threshold is reached
    curr_sum = 0
    for curr_num in range(1, threshold): # exclude 0 & threshold
        if (curr_num % 3 == 0 or curr_num % 5 == 0):
            curr_sum += curr_num

    return curr_sum


if __name__ == "__main__":
    # Initial test: threshold = 10 --> sum = 23
    case_1_sum = sum_multiples_3_5(10)
    assert case_1_sum == 23

    # Test case: threshold = 1000
    test_case_sum = sum_multiples_3_5(1000)
    print("Total sum of multiples below 1000:", test_case_sum)