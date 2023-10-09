"""
PROGRAM NAME - reverse_string
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python + numpy
SYSTEM - Windows 11
DATE - Completed 21/06/2023
NDP - None :)
"""

def reverse_string(text):
    """
    Reverse the way of the string (letters + words)
    
    Args:
        text (string): sentence to reverse.
    
    Returns:
        text (string): reversed sentence.
    """
    
    text = text.split()
    text = text[::-1]
    
    for i in range(len(text)):
        text[i] = text[i][::-1]
    
    text = ' '.join(text)
    
    return text
    

# Test the function
text = "Hello, World!"
print(reverse_string(text))
