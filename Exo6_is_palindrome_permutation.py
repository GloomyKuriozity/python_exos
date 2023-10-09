"""
PROGRAM NAME - is_palindrome_permutation
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 03/08/2023
NDP - depends on collections library
"""

from collections import Counter

def is_palindrome_permutation(text):
    """
    Will test if a word can be a palindrome with any type of permutation.
    
    Args:
        text (string): string to test.
    
    Returns:
        bool (bool): true if palindrome, else false.
    """
    odd_count = 0
    
    text = text.replace(' ','')   
    char_count = dict(Counter(text.lower()))
    
    for i in char_count.values():
        if i%2 != 0:
            odd_count += 1
    
    if odd_count > 1:
        return False
    else:
        return True
    
    
# Test the function
text = "tactcoa"
print(is_palindrome_permutation(text))
