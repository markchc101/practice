"""
Solve a Kakuro item.

Given:
    S - the sum, 
    N - number of slots 
    P - you can use numbers between 1 - P 
    
You should only use a number once and same numbers are considered as the same 
solution. 

Example: 
    S=6, 
    N=2, 
    P=6 
    
Answers: 
    1. 4,2 
    2. 5,1 
    3. 3,3

4337714987 
"""

def solve_kakuro(S: int, N: int, P: int):
    """
    """
    # Generate a list of USABLE numbers. A number is usable only if it is 
    # smaller than the sum.
    viable_numbers = [i for i in range(1, P+1)]

    all_sets = set()

    def findvia
    for i in viable_numbers:

        n_set = set()
        while len(n_set) < N:
            remainder = S - i

            new_numbers = [j for j in viable_numbers if j < remainder]
            if set_size < N:



        def f(i):
            viable_numbers
            