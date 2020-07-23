#Simple programs to check id two strings are anagram or not
#Algorithm 1
def anagram_checker1(s1,s2):
    ''' 
    INPUT = str,str
    OUTPUT = bool
    '''
    # reomoving non-alphanumeric chars and sorting comparing
    s1 = ''.join(filter(str.isalnum, s1.lower()))
    s2 = ''.join(filter(str.isalnum, s2.lower()))

    return sorted(s1) == sorted(s2)

#algorithm 2
from collections import defaultdict
def anagram_checker2(s1,s2):
    '''
    INPUT = str,str
    OUTPUT = bool
    '''
    s1 = ''.join(filter(str.isalnum, s1.lower()))
    s2 = ''.join(filter(str.isalnum, s2.lower()))
    if len(s2) != len(s1):
        return False
    letters = defaultdict(int)
    for letter in s1:  #searching and adding char in s1 to dict
        letters[letter] += 1
    
    for letter in s2: #searching and substracting char in s2 from dict
        if letters[letter] == 0:
            return False
        else:
            letters[letter] -= 1
    return True

if __name__ == "__main__":
    s1 = "public relations"
    s2 = "crap built on lies."
    print(anagram_checker1(s1,s2))
    print(anagram_checker2(s1,s2))