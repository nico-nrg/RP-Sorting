import sys
import random

# =========================================================================
def random_number(N):
	minimum = pow(10, N-1)
	maximum = pow(10, N) - 1
	return random.randint(minimum, maximum)

# =========================================================================
args = len(sys.argv) - 1
if (args < 1):
   print("Cara menggunakan : python3 " + sys.argv[0] + " jumlah_data\n")
   sys.exit(0)

jumlah_data = sys.argv[1]
nama_file = "file_" + jumlah_data + ".dat"

file = open(nama_file, 'w')
i=1
while i <= int(jumlah_data):
   file.write(str(random_number(10)) + '\n')
   i += 1

file.close
