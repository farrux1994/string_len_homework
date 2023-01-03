def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    palindrome = len(s)
    if palindrome == 3:
        return False
    else:
        return True
y = main('cff')
print(y)        