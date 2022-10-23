ex_str = '{} Samuels learning python'

#trying dif. string functions
# .format() function changes place holders into what string value you set

ex_str2 = ex_str.format('Aiden')
print(ex_str2)

sent = '{} is a good {}, he {}\'s everyday'.format('white', 'cat', 'play')
print(sent)

# .split(), splits a string into a list of strings, you can specify what seps the items
sent1 = sent.split()
print(sent1)
sent2 = sent.split(", ")
print(sent2)

# .join(), joins items in an iterable into one string with the specified separator
place = ('1', '2', '3')
place2 = ',,,'.join(place)
print(place2)

# .strip() removes whitespace from the leading and trailing ends of a string
ex = '   my name  '.strip()
print(ex)

# .format_map() i dont know how to describe this any other way than substitution jutsu 
ex = {'name': 'john', 'lname': 'wick'}
state = 'his name is {name} {lname}'
print(state.format_map(ex))

# .upper() converts to uppercase
# .lower() converts to lowercase