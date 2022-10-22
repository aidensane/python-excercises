# a program to display the frequency of chars in a string
from collections import Counter

user = 'Hello everyone'
res = Counter(user)
print('Count of all chars in string: \n' + str(res))