for letter in 'arrakisarrakis':
    if letter == 'a' or letter == 'k':
        continue
    print('current letter: ', letter)
print(' ')
for letter in 'arrakisarrakis':
    if letter == 'r' or letter == 's':
        break
    print('current letter: ', letter)
print(' ')
#We use pass statement in Python to write empty loops.
#Pass is also used for empty control statements, functions and classes.
#it doesn’t perform any specific action within the loop, and the ‘pass' statement is used.
# After the loop, it prints “Last Letter :”
# followed by the last character in the string, which is ‘s’
for letter in 'arrakisarrakis':
    pass
print('last letter: ', letter)
