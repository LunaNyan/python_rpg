#!/usr/bin/python3

import sys

#def
def exit(exitmessage):
    if exitmessage == '':
        exitmessage = 'no dying message provided'
    sys.exit(exitmessage)

def level_2_a():
    print ('you are in level_2_a')
    exit('exit at 2a')

def level_2_b():
    print ('you are in level_2_b')
    exit('exit at 2b')

print ('first entry')
print ('1 : goto A')
print ('2 : goto B')

while 1:
    inp = input ('your selection : ')
    if inp == '1':
        level_2_a()
    elif inp == '2':
        level_2_b()
    else:
        print ('what?')
        continue
