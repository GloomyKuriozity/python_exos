"""
PROGRAM NAME - fibonacci_sequence
PROGRAMMER - Kuriozity
LANGUAGE - Python (no add-on libraries)
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""

def fibonacci(n):
    sequence = [0,1]

    for count in range(2,n):
        sequence.append(sequence[count - 1] + sequence[count])

    return sequence

# Test the function
n = 10
print(fibonacci(n))
