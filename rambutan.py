jumlahRambutanIpin = int(input("Masukan jumlah rambutan ipin = "))
jumlahRambutanUpin = int(input("Masukan jumlah rambutan upin = "))

def rambutanUntukKakRos(upin, ipin):
  if(upin < ipin) :
    return upin
  elif(ipin < upin) :
    return ipin
  else:
    return 0

print("Rambutan untuk kak ros = ", rambutanUntukKakRos(jumlahRambutanUpin, jumlahRambutanIpin))
