def string_pig_latin(str):
  words = str.split()
  new_str = ""
  vowels = ['a','e','i','o','u']
  for word in words:
    new_str = f"{new_str}{word}ay " if word[0] in vowels else f"{new_str}{word[1:len(word)]}{word[0]}ay "
  return new_str

print(string_pig_latin("all open bndroids"))
print(string_pig_latin("python code wins"))