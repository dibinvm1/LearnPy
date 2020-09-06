'''
Given a string function to return a list of all possible permutaions
'''
def string_permutation(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i,char in enumerate(s):
            for perm in string_permutation(s[:i]+s[i+1:]):
                out +=[char+perm]
    return out

print(string_permutation('abc'))
    