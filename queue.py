queueList = []
def main():
  print("=================================")
  print("1. Buat antrian")
  print("2. Panggil antrian selanjutnya")
  print("=================================")
  command = int(input("Pilih salah satu dari diatas = "))
  if(command == 1):
    queue()
  elif(command == 2):
    dequeue()
  else:
    print("Input Tidak valid")
  main()
def queue():
  queueList.append(len(queueList) + 1)
  print("")
  print("=============================================================")
  print("Antrian nomor {} berhasil dibuat".format(queueList[len(queueList) - 1 ]))
  print("Nomor antrian saat ini {}".format(",".join(str(x) for x in queueList)))
  print("=============================================================")
  print("")
def dequeue():
  if(len(queueList) == 0):
    print("")
    print("=============================================================")
    print("Sudah tidak ada antrian")
    print("=============================================================")
    print("")
  else:
    print("")
    print("=============================================================")
    print("Antrian nomor {} silahkan menuju loket".format(queueList[0])) 
    queueList.pop(0)
    if(len(queueList) == 0):
      print("Sudah tidak ada antrian")
    else:
      print("Nomor antrian saat ini {}".format(",".join(str(x) for x in queueList)))
    print("=============================================================")
    print("")
main()