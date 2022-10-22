# a program to return the first 2 and last 2 chars of a string, if string is < 2 chars return nothing
def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]

print(string_both_ends('hello everyone'))