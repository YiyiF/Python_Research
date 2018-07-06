# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:41:06 2018

@author: eleve
"""
# E1
import string
string.ascii_lowercase
alphabet = ' ' + string.ascii_lowercase

# E2
positions = {alphabet[i]:i for i in range(0,27)}

# E3
message = "hi my name is caesar"
alphabet_len = len(alphabet)
positions_key1 = {alphabet[i]:((i + 1) % alphabet_len) for i in range(alphabet_len)}
encoded_message = ''.join([alphabet[positions_key1[letter]] for letter in message])

positions_key1 = {}
for i in range(alphabet_len):
    positions_key1[alphabet[i]] =((i + 1) % alphabet_len)

encoded_message = ""
for letter in message:
    encoded_message += alphabet[positions_key1[letter]]

# E4
def encoding(message, key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
        encoded_string = "".join(encoding_list)
    return encoded_string

encoded_message = encoding(message, 3)
print(encoded_message)

# E5
decoded_message = encoding(encoded_message, -3)
print(decoded_message)




