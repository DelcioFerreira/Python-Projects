#RandomPassWordGenerator

import random

#form the random letters with random and assign them to a variable

upperCaseLetter = chr(random.randint(65,90))
upperCaseLetter2 = chr(random.randint(65,90))
lowercaseletter = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
randomPunct = chr(random.randint(33,38))

password = upperCaseLetter + upperCaseLetter2 + lowercaseletter + lowercaseletter2 + digit1 + digit2 + randomPunct

print(password)