# a program to change all instances of the first char of a string to $ apart from the first instance itself
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1
print(change_char('hello there'))