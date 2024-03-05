# iterate over each character in length of string
# if (even) no remainder when divided by 2, add upper case character to the string
# if odd, add lower case character to the string
# this will cause string to alternate every character between upper and lower case
test_str = "This is my test string"
char = []

for i in range(len(test_str)):
    if i % 2 == 0:
        char.append(test_str[i].upper())
    else:
        char.append(test_str[i].lower())
new_str = ''.join(char)
print(new_str)

# iterate over each word in length of string
# if iteration is even, add entire word in upper case to the string
# this will cause string to alternate every character between upper and lower case
second_string = "This is my second test string"
words = second_string.split()

for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].upper()
    else:
        words[i] = words[i].lower()

mod_string = ' '.join(words)
print(mod_string)
