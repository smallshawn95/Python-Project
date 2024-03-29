import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
length = 16

password = ''.join(random.sample(chars, length))

print(password)
