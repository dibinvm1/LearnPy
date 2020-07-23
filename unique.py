'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
'''
def unique_string(s):
    chars = set()
    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True
print(unique_string('abcsdfeg'))


def unique_string2(s):
    return (len(s) == len(set(s)))
print(unique_string('abcsdfeg'))