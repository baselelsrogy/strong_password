# 1- import string module
# 2- store all characters in lists (upper/lower case, digits, punctuations)
# 3- take number of characters from users
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digits and punctuations

# import string module
import string

import random

# store all characters in lists (upper/lower case, digits, punctuations)
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# take number of characters from users
character_numbers = input("How many characters for the password?: ")

# make sure the number of characters is 6 or more
while True:
    try:
        character_numbers = int(character_numbers)
        if character_numbers < 6 :
            print("You need at least 6 characters")
            character_numbers = input("Please enter the number again: ")
        else:
            break
    except :
        print("Please enter numbers only")
        character_numbers = input("How many characters for the password?: ")

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# calculate 30% and 20% of number of characters
part1 = round(character_numbers * (30/100))
part2 = round(character_numbers * (20/100))


# create password 60% letters and 40% digits and punctuations
password = []

for i in range(part1) :
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2) :
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

# Final result
print(f"your password is => {password}")