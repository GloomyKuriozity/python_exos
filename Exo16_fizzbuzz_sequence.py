"""
PROGRAM NAME - fizzbuzz_sequence
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python (no add-on libraries)
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""
def fizzbuzz(n):
    """
    Display numbers from 1 to n, but replace:
     - with 'Fizz' numbers dividable by 3
     - with 'Buzz' numbers dividable by 5
     - with 'FizzBuzz' numbers dividable by 3 and 5.
    
    Args:
        n (int): The number of value to test and display.
    
    Returns:
        None.
    """
    for count in range(1,n+1):
        if count % 3 == 0:
            if count % 5 == 0:
                print('FizzBuzz')
            else :
                print('Fizz')
        else:
            if count % 5 == 0:
                print('Buzz')
            else:
                print(count)

# Test the function
n = 15
fizzbuzz(n)
