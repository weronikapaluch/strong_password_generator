import random as random
import string

password = ""
for i in range(10):
    password += random.choice(string.ascii_letters)

print(password)

