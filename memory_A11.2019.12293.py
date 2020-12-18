# A11.2019.12293
# Dhevan Muhamad Anthareza
def calc():
  print("Kalkulator Sederhana Untuk Menghitung Alamat Memori")
  print("Masukkan alamat segment dan offset dengan format")
  memoryAddress = input("segment:offset = ")
  segment, offset = memoryAddress.split(":")
  segment = segment.ljust(5, '0')
  offset  = "0x{}".format(offset)
  intSegment = int(segment, 16)
  intOffset = int(offset, 16) 
  alamatFisik = hex(intSegment + intOffset)
  intAlamatFisik = int(alamatFisik, 16)

  print("Segment  =    ", segment," ===> ", intSegment)
  print("Offset   =    ", offset, " ===> ", intOffset)
  print("===========================================================")
  print("Segment      = {}".format(segment.rjust(10, ' '))) 
  print("Offset       = {}".format(offset.rjust(10, ' ')))
  print("               ".ljust(28, '-'), "+")
  print("")
  print("Alamat Fisik =    ", alamatFisik, " ===> int =   ", intAlamatFisik)
  print("===========================================================")
  confirmation = input("Apakah ingin mengulangi proses [1=Ya | 0=Exit] ? ")
  if(confirmation == '1'):
    calc()
calc()