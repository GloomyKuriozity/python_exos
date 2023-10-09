"""
PROGRAM NAME - palindrome_checker
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python (no add-on libraries)
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""

def is_palindrome(text):
    """
    Check if the text is a palindrome.
    
    Args:
        text (string): The text to be checked.
    
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """

    text = text.replace(" ","")
    text = text.lower

    text_new = text[::-1]

    if text_new == text:
        return True
    else:
        return False

# Test the function
text = 'radar'
print(is_palindrome(text))
