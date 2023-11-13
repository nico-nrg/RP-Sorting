import sys
import random
import string
import secrets

# =========================================================================
def random_string():
        minimum = 10
        maximum = 20
        num = random.randint(minimum, maximum)
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
        return res

# =========================================================================
args = len(sys.argv) - 1
if (args < 1):
   print("Cara menggunakan : python3 " + sys.argv[0] + " jumlah_data\n")
   sys.exit(0)

jumlah_data = sys.argv[1]
nama_file = "file_string_" + jumlah_data + ".dat"

file = open(nama_file, 'w')
i=1
while i <= int(jumlah_data):
   file.write(random_string() + '\n')
   i += 1

file.close
