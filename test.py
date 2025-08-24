cases = ["()", "()[]{}", "(]", "([])", "([)]"]

number = 1
for case in cases:
    print(f"Case {number}")
    number += 1
    result = isValid(case)
    print(f"\tResult: {result}")

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    symbols = {'(': ')', '[': ']', '{': '}'}
    keys = symbols.keys()
    values = symbols.values()

    ending_of_openings = ''
    endings_in_string = ''

    for char in s:
        if char in values:
            endings_in_string += char
        elif char in keys:
            ending_of_openings += symbols[char]
        else:
            return False
    print(f"\tEndings_in_case: {endings_in_string}\n\tEndings of Openings: {ending_of_openings}")
    if endings_in_string != ending_of_openings:
        return False

    return True 
