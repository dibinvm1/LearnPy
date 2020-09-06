'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
'''
#RunLength - O(n) Space - O(n)
def string_compress(s):
    size = len(s)
    if size == 0:
        return ''
    if size == 1:
        return s+'1'
    temp = ''
    i = 1
    cnt = 1
    while i < size:
        if s[i] == s[i-1]:
            cnt +=1
        else:
            temp = temp + s[i-1]+ str(cnt)
            cnt = 1
        i += 1
    temp = temp + s[i-1]+ str(cnt)
    return (temp)
print(string_compress('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))