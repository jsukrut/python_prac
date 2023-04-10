import string

print(string.ascii_letters)
print(string.ascii_uppercase)
char_occur ={}
for letter in string.ascii_uppercase:
    char_occur.update({letter:0 })

for letter in string.ascii_letters:
    char_occur.update({letter:0 })

print(char_occur)

para = input("Enter Paragraph")
#
for char in para:
    if char in char_occur.keys():
        char_occur[char] = char_occur[char] + 1

print(char_occur)