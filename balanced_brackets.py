'''
Checking if given string of parathesis is balanced assumes string has only parathesis
'''
def balance_check(s):
    matching_sets = set([('(',')'),('[',']'),('{','}')])
    stacks = []
    for bracket in s:
        if bracket == '[' or bracket == '{' or bracket == '(':
            stacks.append(bracket)
        else:
            if len(stacks) == 0:
                return False
            last_opened = stacks.pop()
            if (last_opened,bracket) not in matching_sets:
                return False
    return len(stacks) == 0


s = '[[[]]]{}()()'
print(balance_check(s))
