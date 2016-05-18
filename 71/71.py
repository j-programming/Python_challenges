# -*- coding: utf-8 -*-
import math
print('Task 71: Triangle number calc')

def printRow(spaces,dots):
	#stri=''
	#for num in(0,spaces):
	stri='' + spaces*" "
	for num in range(0,dots):
		stri=stri+"* "
	print stri
	

raw_h=raw_input("Enter number: ")
height=int(raw_h)

complete=height*2-1
deep=height-1
current=1

while (current<=height):
	printRow(deep,current)
	deep=deep-1
	current=current+1

print('Thanks4using')