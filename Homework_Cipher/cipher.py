# 1. Write the program to encrypt the text file (case insenstive) into cipher text
# 2. Write the program to decrypt the cipher text to plain text(normal text- case insensitive) 
# Shift is 5

import string

# ask user if encrypt or decrypt
def cipherFunction():
	while True:
			print ("")
			print ("___________________________________________________________________________________")
			print ("Do you want to encrypt or decrypt Cipher text? Press a to encrypt and b to decrypt:")
			cipher = input()
			if cipher == "a":
				return cipher
			elif cipher == "b":
				return cipher
			else:
				print ("")
				print ("Please select a or b:")
				

cipherFunction = cipherFunction()

# ask user input
def userMessage():
	while True:
			print ("")
			print ("Enter message:")
			user = input()
			return user

userMessage = userMessage()

# string of both uppercase/lowercase letters
alph_string = string.ascii_letters

# encrypt message
if cipherFunction == "a":

		def shift_this_string(string, shift):

		     return ''.join([chr(ord(c)+shift) if c in alph_string else c for c in string])

		string = userMessage
		shift = 5 

		print("")
		print("Encrypted message:")
		print(shift_this_string(string, shift))
		print("")

#decrypt  message
elif cipherFunction == "b":

		def shift_this_string(string, shift):

		     return ''.join([chr(ord(c)+shift) if c in alph_string else c for c in string])

		string = userMessage
		shift = -5

		print("")
		print("Decrypted message:")
		print(shift_this_string(string, shift))
		print("")

