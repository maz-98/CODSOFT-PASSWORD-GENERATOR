import string
import random

s1 = string.ascii_uppercase
#print(s1)
s2 = string.ascii_lowercase
#print(s2)
s3 = string.digits
#print(s3)
s4 = string.punctuation
#print(s4)
plen = int(input("Enter Password Length (Make sure that ,you use integers for password length)\n"))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s)
random.shuffle(s)
#print(s)
print("".join(s[0:plen]))