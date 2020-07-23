'''
printing Reverse of a sentance or return in Function
'''
#Return in a Function Time - O(n)
import collections
def sentence_rev(s):
    string = collections.deque()
    size = len(s)
    spaces = [' ']
    i = 0
    while i < size:
        if s[i] not in spaces:
            word_start = i
            while i < size and s[i]  not in spaces:
                i +=1
            string.appendleft(s[word_start:i])
        i += 1
    return (" ".join(string))
print(sentence_rev('    This Sentence has Space Before and  after    '))

# Printing reversed String
s= '    This Sentence has Space Before and  after    '
word_stack = []
for word in s.split():
    word_stack.append(word)
for i in range(len(word_stack)):
    print(word_stack.pop(),end =" ")