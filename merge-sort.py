# Program merge sort array
# Cara menggunakan phyton3 merge-sort.py [nama_file]
# Apabila tidak diikuti file yang akan diproses, maka program akan menggunakan
# data yang sudah ada di dalam program
# File yang akan diproses berupa file teks yang berisi data.


import sys
import time

print("Merge Sort") 

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)
    if len(sys.argv) == 1:
      print("Kiri   : ", end=" ")
      for i in left_half:
        print(i, end = ' ')
      print("")
      #print("Pivot  : \033[1;32;40m% d\033[1;37;40m" % mid, end=" ")
      #print("")
      print("Kanan  : ", end=" ")
      for i in right_half:
        print(i, end = ' ')
      print("\n")

    merged_arr = merge(left_half, right_half)
    return merged_arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result
 
 
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
mergeSort(arr)
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
