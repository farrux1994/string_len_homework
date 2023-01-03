def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    c = len(a)
    if c%2 == 0:
        return True
    else:
        return False

y = main('code')
print(y)