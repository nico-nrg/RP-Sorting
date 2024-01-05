# Program selection sort
# Cara menggunakan phyton3 selection-sort.py [nama_file]
# Apabila tidak diikuti file yang akan diproses, maka program akan menggunakan
# data yang sudah ada di dalam program
# File yang akan diproses berupa file teks yang berisi data.

import sys
import time

print("Selection Sort")

def selectionSort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                 
        # Swap the found minimum element with
        # the first element       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Apabila tidak ada parameter tambahan, tampilkan array yang diproses
        if len(sys.argv) == 1:
          for j in range(len(arr)):
            if (j == i):
              print("\033[1;32;40m% d" % arr[j], end=" ")
            elif (j == min_idx):
              print("\033[1;33;40m% d" % arr[j], end=" ")
            else:
              print("\033[1;37;40m% d" % arr[j], end=" ")

        if len(sys.argv) == 1:
          print("\033[1;31;40m\n============================\n\033[1;37;40m")

     
    return
 
if len(sys.argv) == 1:
  # Apabila tidak ada file yang akan diproses, maka arr akan menggunakan default
  # dari program
  arr = [64, 34, 25, 12, 22, 11, 90]
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
      try:  
        t = int(list[i])
      except:
        t = list[i]

      arr.append(t)

  # Tampilkan jumlah data
  #print(len(arr))

 
# Simpan waktu mulai
start_time = time.time()
selectionSort(arr)
# Simpan waktu selesai
end_time = time.time()
 
if len(sys.argv) == 1:
  print("Array yang sudah diurutkan :", end=" ")
  for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
  print("\n")

jumlah_data = "{:,}".format(len(arr))
print("Jumlah data yang diproses  : %s" % jumlah_data)
print("Lama pengurutan            : %.5f detik\n\n" % round((end_time - start_time), 5))

