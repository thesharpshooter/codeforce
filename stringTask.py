#Convert string to a new string that follow:
    # consonant --> .consonant
    # vowel --> delete them
    # everythin to lower case

string = raw_input()
string = string.lower()
new_string = ""
vowels = ["a","e","i","o","u","y"]
for x in string:
    if x not in vowels:
        new_string += "."+x

print new_string
