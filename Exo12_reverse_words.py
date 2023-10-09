"""
PROGRAM NAME - reverse_words
PROGRAMMER - Mélanie Geulin (melanie.geulin@gmail.com)
LANGUAGE - Python (no add-on libraries)
SYSTEM - Windows 11
DATE - Completed 20/06/2023
BUGS - None :)
"""
def reverse_words(sentence):
    """
    Reverse the words in a sentence.
    
    Args:
        sentence (string): Sentence to reverse.
    
    Returns:
        rev_sentence (string): Reversed sentence.
    """
    rev_sentence = sentence.split()
    rev_sentence = rev_sentence[::-1]
    rev_sentence = ' '.join(rev_sentence)

    return rev_sentence

# Test the function
sentence = "I am a programmer"
print(reverse_words(sentence))
