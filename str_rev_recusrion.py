'''
String reverse using Recursion
'''

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse (s[1:]) + s[0]
print(reverse("HI"))
print(reverse('hello world this is a long string'))
print(reverse('123456789'))