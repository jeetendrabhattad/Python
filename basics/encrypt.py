def helper(message, shift):
	message = message.lower()
	secret = ""
	print 'Inside Helper Function'
	for c in message:
		if c in "abcdefghijklmnopqrstuvwxyz":
			num = ord(c)
			num += shift
			if num > ord("z"):     # wrap if necessary
				num -= 26
			elif num < ord("a"):
				num += 26
			secret = secret + chr(num)
		else:
			# don't modify any non-letters in the message; just add them as-is
			secret = secret + c
	return secret

# Encrypts the given string using a Caesar cipher and returns the result.
def encrypt(message):
	print 'Called Encrypt Function'
	return helper(message, 3)

# Decrypts a string that was previously encrypted using a Caesar cipher and returns the result.
def decrypt(message):
	return helper(message, -3)


# main program
msg = raw_input("Your message to encode? ")
if len(msg) > 0:
	# wants to encrypt
	secret = encrypt(msg)
	print("The encoded message is:", secret)
else:
	# empty message; wants to decrypt
	secret = raw_input("Your message to decode? ")
	if len(secret) > 0:
		msg = decrypt(secret)
		print("The decoded message is:", msg)
