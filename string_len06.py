def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    if len(str(s1)) < len(str(s2)):
        return s1
y = main('code', 'python')
print(y)