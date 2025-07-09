def length_of_last_word(s: str) -> int:
    """
    Given a string s consisting of words and spaces, return the length of the last word.
    A word is a maximal substring consisting of non-space characters only.
    """
    # Trim trailing spaces and split by spaces
    words = s.strip().split()

    # If there are no words, return 0
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])
