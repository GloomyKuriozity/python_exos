"""
PROGRAM NAME - check_anagrams
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 21/06/2023
NDP - None :)
"""

def check_anagrams(str_1, str_2):
    """
    Check if two words are anagrams of each other.
    
    Args:
        str1 (string): first word to test.
        str2 (string): second word to test.
    
    Returns:
        bool (bool): True if anagrams, False if not.
    """    
    
    return sorted(str_1.replace(' ','')) == sorted(str_2.replace(' ',''))
    

# Test the function
str1 = "listen"
str2 = "silent"
print(check_anagrams(str1, str2))
