# Program quick sort array
# Cara menggunakan phyton3 quick-sort.py [nama_file]
# Apabila tidak diikuti file yang akan diproses, maka program akan menggunakan
# data yang sudah ada di dalam program
# File yang akan diproses berupa file teks yang berisi data.


import sys
import time


print("Quick Sort") 

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    if len(sys.argv) == 1:
      print("Array  : ", end=" ")
      for i in arr:
         print(i, end = ' ')
      print("")

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    global step_counter
    step_counter += 1

    if len(sys.argv) == 1:
      print("Kiri   : ", end=" ")
      for i in left:
        print(i, end = ' ')
      print("")
      print("Pivot  : \033[1;32;40m% d\033[1;37;40m" % pivot, end=" ")
      print("")
      print("Kanan  : ", end=" ")
      for i in right:
        print(i, end = ' ')
      print("\n")

    return quickSort(left) + middle + quickSort(right)
 
step_counter = 0

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
sorted_array = quickSort(arr)
end_time = time.time()
 
# Apabila tidak ada parameter tambahan, tampilkan array yang diproses
if len(sys.argv) == 1:
  print("Array yang sudah diurutkan :", end=" ")
  for i in range(len(sorted_array)):
    print("% d" % sorted_array[i], end=" ")
  print("")

jumlah_data = "{:,}".format(len(arr))
print("Jumlah data yang diproses  : %s" % jumlah_data)
print("Lama pengurutan            : %.5f detik\n\n" % round((end_time - start_time), 5))

