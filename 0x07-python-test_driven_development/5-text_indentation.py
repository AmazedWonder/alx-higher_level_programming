#!/usr/bin/python3
"""Defines a function that prints a text with 2
new lines after each of these characters: ., ? and :

first checks if the text parameter is a string.
If it's not, a TypeError is raised.

print the text with two new lines after each occurrence of
'.', '?', and ':', while removing any leading spaces on each line.
It uses a loop to iterate through each character in the text string
and performs the necessary checks and printing operations.

The text_indentation function takes a string text as input
and prints the formatted text with two new lines after each
occurrence of '.', '?', and ':'. Leading and trailing spaces
on each line are removed. The function processes the input text
character by character, identifies the specified punctuation marks,
and formats the text accordingly.

Parameters:

text (str): The input text to be formatted.
Exceptions:

TypeError: Raised when the text parameter is not a string.

"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello
        How are you
        I'm fine

        >>> text_indentation("This is a test: one. two? three: four.")
        This is a test
        one
        two
        three
        four

        >>> text_indentation("")
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_index = 0
    # Skip leading spaces
    while char_index < len(text) and text[char_index] == ' ':
        char_index += 1

    while char_index < len(text):
        print(text[char_index], end="")
        # Checkss if the current character is a newline
        # or one of the punctuation characters
        if text[char_index] == "\n" or text[char_index] in ".?:":
            if text[char_index] in ".?:":
                # Print an extra newline after punctuation characters
                print("\n")
            char_index += 1
            # Skip consecutive spaces
            while char_index < len(text) and text[char_index] == ' ':
                char_index += 1
            continue
        char_index += 1
