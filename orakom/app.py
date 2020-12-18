from tabulate import tabulate
import itertools as it
def genConverter(angka, basis):
    result = []
    hasilAngka = ""
    loop = True
    while loop:
        if angka >= basis:
            result.append(" {}".format(angka))
            sisa = angka % basis
            angka = angka // basis
            if sisa > 9:
                huruf = libChar(sisa)
                hasilAngka += huruf
                sisa = "{} = {}".format(sisa, huruf)
            else:
                hasilAngka += str(sisa)
            divid = "{}------  {}".format(basis, sisa)
            result.append(divid)
        else:
            if angka > 9:
                angka = libChar(angka)
            hasilAngka += str(angka)
            result.append(angka)
            loop = False
            break
    
    hasilAngka = "".join(reversed(hasilAngka)) #reversed

    return (result, hasilAngka)
def libChar(angka):
    if angka == 10:
        return "A"
    elif angka == 11:
        return "B"
    elif angka == 12:
        return "C"
    elif angka == 13:
        return "D"
    elif angka == 14:
        return "E"
    elif angka == 15:
        return "F"
    elif angka == 16:
        return "G"

angka = int(input("Masukkan bilangan untuk dikonversi : "))
biner, hasilBiner = genConverter(angka, 2)
octal, hasilOctal = genConverter(angka, 8)
hexa, hasilHexa = genConverter(angka, 16)

table = list(it.zip_longest(biner, octal, hexa))
print(table)

# # ini untuk header table
# header = ("Binner", "Octal", "Hexadecimal")

# print(tabulate(table, header, tablefmt="plain"))
# print("")
# print("==============================================================")
# print("Binner : ", hasilBiner)
# print("Octal  : ", hasilOctal)
# print("Hexa   : ", hasilHexa)
