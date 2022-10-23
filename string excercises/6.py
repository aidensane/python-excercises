# a program to accept a file name and then print just the extension type of the file
filename = input('input a file name(ex: learning.py ): ')
ext = filename.split('.', 1)
print(ext[1]) 