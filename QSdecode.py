#!/usr/bin/python3

# hints for the lazy: this file can be run or find the clues here

import base64

encodedStr = input("Please enter hash: ")

try:
	decodedBytes = base64.urlsafe_b64decode(encodedStr)
except:
	print("Invalid value for this type of hash")
	exit()

decodedStr = str(decodedBytes, "utf-8")


print(decodedStr)

