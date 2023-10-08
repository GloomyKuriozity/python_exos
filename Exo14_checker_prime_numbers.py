"""
PROGRAM NAME - checker_prime_numbers
PROGRAMMER - Kuriozity
LANGUAGE - Python + [math]
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""

import math

def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to be checked.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num == 2:
        return True
    if num <= 1:
        return False

    sqrt_num = int(math.sqrt(num)) + 1
    
    for count in range(2, sqrt_num):
        if num % count == 0:
            return False
        
    return True

# Test the function
num = 12
print(is_prime(num))
