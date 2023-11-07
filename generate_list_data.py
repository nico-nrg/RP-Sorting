import random
import string

file = open('file.dat', 'w')

i=1
while i <= 100:
  teks = ''.join(random.choices(string.ascii_lowercase, k=10))
  file.write(teks + '\n')
  i += 1

file.close

