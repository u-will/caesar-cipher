import string
def encrypt(plain, num):
  newString= ''
  for char in plain:
    if string.ascii_lowercase.__contains__(char) or string.ascii_uppercase.__contains__(char):
      charNum = ord(char) + num
      if charNum > 122:
        charNum = charNum - 26
      char = chr(charNum)
    newString += char
  return newString


def decrypt(plain, num):
  return encrypt(plain, -num)