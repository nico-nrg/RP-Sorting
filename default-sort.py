# Program default sort dari python
# Cara menggunakan phyton3 default-sort.py [nama_file]
# Apabila tidak diikuti file yang akan diproses, maka program akan menggunakan
# data yang sudah ada di dalam program
# File yang akan diproses berupa file teks yang berisi data.


import sys
import time

print("Default Sort") 

if len(sys.argv) == 1:
  # Apabila tidak ada file yang akan diproses, maka arr akan menggunakan default
  # dari program

  arr = [64, 34, 25, 12, 22, 90, 11]
  print("Array awal : ", end=" ")
  for i in arr:
     print(i, end = ' ')
  print("\n")

else:
  # buka file yang ada di argumen.
  file = open(sys.argv[1], "r")
  contents = file.read()
  list = contents.split("\n")
  file.close()

  arr = []
  for i in range(len(list)):
    if (list[i] != ''):
      t = int(list[i])
      arr.append(t)

  #print(arr)
  #print(len(arr))
 
start_time = time.time()
arr.sort()
end_time = time.time()
 
# Apabila tidak ada parameter tambahan, tampilkan array yang diproses
if len(sys.argv) == 1:
  print("Array yang sudah diurutkan :", end=" ")
  for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
  print("")

jumlah_data = "{:,}".format(len(arr))
print("Jumlah data yang diproses  : %s" % jumlah_data)
print("Lama pengurutan            : %.5f detik\n\n" % round((end_time - start_time), 5))
