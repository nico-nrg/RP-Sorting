# Program bubble sort array
# Cara menggunakan phyton3 bubble-sort.py [nama_file]
# Apabila tidak diikuti file yang akan diproses, maka program akan menggunakan
# data yang sudah ada di dalam program
# File yang akan diproses berupa file teks yang berisi data.


import sys
import time

print("Bubble Sort") 

def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        # Apabila tidak ada parameter tambahan, tampilkan array yang diproses
        if len(sys.argv) == 1:
          for k in range(len(arr)):
            if (k == 0):
              print("\033[1;32m% d" % arr[k], end=" ")
            else:
              print("\033[1;37;40m% d" % arr[k], end=" ")
          print("")

            #if ((i % 100) == 0):
              #print(".", end="")

        for j in range(0, n-i-1):
 
            # Telusuri array dari 0 sampai n-i-1
            # tukar apabila ditemukan data yang lebih besar
            # daripada data berikutnya
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Apabila tidak ada parameter tambahan, tampilkan array yang diproses
                if len(sys.argv) == 1:
                  for i in range(len(arr)):
                    if (i == j+1):
                      print("\033[1;32m% d" % arr[i], end=" ")
                    else:
                      print("\033[1;37;40m% d" % arr[i], end=" ")         
                  print("")         

                  if ((i % 100) == 0):
                    print(".", end="")

        if len(sys.argv) == 1:
           print("\033[1;31;40m\n============================\n\033[1;37;40m")

        if not swapped:
            # jika tidak ada lagi data yang diproses
            # keluar dari loop
            return
 
 
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
bubbleSort(arr)
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
