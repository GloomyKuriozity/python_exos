"""
PROGRAM NAME - longest_substring
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 08/08/2023
NDP - None :)
"""



def longest_substring(text):
    """
    Will return the length of the longest possible substring from the given string where there's no character repeating itself.
    
    Args:
        text (string): string to test.
    
    Returns:
        max_length (int): maximum length without repeating character.
    """
    
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(text):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
    
    
# Test the function
text = "abcabcbb"
print(longest_substring(text))
