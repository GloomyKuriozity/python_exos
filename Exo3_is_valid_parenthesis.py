"""
PROGRAM NAME - is_valid_parentheses
PROGRAMMER - Kuriozity
LANGUAGE - Python 
SYSTEM - Windows 11
DATE - Completed 10/08/2023
NDP - None :)
"""



def is_valid_parentheses(text):
    """
    Makes sure that the brakets, parenthesis, braces are in the correct position and with the correct number.
    
    Args:
        text (string): string to test.
    
    Returns:
        boolean (bool): true if valid order, else false.
    """
    
    symbol_track = list()
    closing_mapping = {
    '(': ')',
    '[': ']',
    '{': '}'
    }
    
    for keys, values in enumerate(text):
        if values in closing_mapping:
            symbol_track.append(values)
        elif len(symbol_track):
            if closing_mapping.get(symbol_track[-1]) == values:
                symbol_track.pop()
            else:
                return False
        else:
            return False
         
    if len(symbol_track) == 0:
        return True
    else:
        return False


# Test the function
text = "{[()]}()"
print(is_valid_parentheses(text))
