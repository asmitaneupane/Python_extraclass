import onetimepad
cipher = onetimepad.encrypt('Ashmita', 'thiskey')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'thiskey')
print(msg)
