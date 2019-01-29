#!/usr/bin/python3

import sys

#system def
def exit(dyingmessage):
    if dyingmessage == '':
        dyingmessage = 'no dying message provided, aborting'
    sys.exit(dyingmessage)

#stage def
def level_2_a():
    print ('you are in level_2_a')
    exit('exit at 2a')

def level_2_b():
    print ('you are in level_2_b')
    exit('exit at 2b')

#frist entry
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
