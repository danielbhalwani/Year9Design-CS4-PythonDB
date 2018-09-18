StringExample.py

#string manipulation
#Strings are collections of characters
#strings are enclosed in "" or ''
#"Paul"
#"Paul is cool"
#"Paul is cool!"

#Two things we need to talk about
#when we think of strings
#index - Always starts at 0
#length

#Example  
# 0123		012345
#"Paul"		"Monkey"
#len("paul") = 4
#len("Monkey") = 6

name = "Paul"  #variable called name

print(name). #I can print strings

sentence = name + " is cool!"
print(sentence)
print(sentence + "!")

#I can access specific letters
fLetter = name[0]	#name at 0
print(fLetter)

letters1 = name[0:2] #inclusive"exclusive
print(letters1)

letters2 = name[2:]
print(letters2)

letters3 = name[:2]
print(letters3)


lname = len(name) #Length of the string
print(lname)

#if I want to print out all letters
for i in range (name):
	print(name[i])










