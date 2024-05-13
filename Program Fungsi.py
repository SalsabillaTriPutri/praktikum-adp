nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"
print()
print(" TUGAS ke 7 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN\n")
print(" Materi : FUNGSI")
print(" Nama   : "+nama)
print(" NIM    : "+nim)
print(" Shift  : "+shift)
print()

def konversi(suhu, satuan):
    while True:
        print("\nBerapa besar suhu yang ingin dikonversi?")
        suhu = int(input("Besar suhu (dalam derajat)  : "))
        print("Apakah satuan dari suhu tersebut?")
        satuan = input("Satuan suhu                 : ")
        satuan = satuan.upper() 
        if satuan not in ['C', 'F', 'R', 'K']:
            print("Satuan suhu tidak valid. Silakan masukkan C, F, R, atau K.")
            continue

        if satuan == 'C':
            if suhu < 0 or suhu > 100:
                print()
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            fahrenheit = int(((9/5) * suhu) + 32)
            reamur = int((4/5) * suhu) 
            kelvin = int(273 + suhu)
            print()
            print("Suhu", suhu ,"derajat", satuan ,"dapat dikonversi menjadi:")
            print()
            print(" ----------------------------")
            print("| SATUAN SUHU | DERAJAT SUHU |")
            print("|----------------------------|")
            print("| Fahrenheit  | {:<12} |".format(fahrenheit))
            print("| Reamur      | {:<12} |".format(reamur))
            print("| Kelvin      | {:<12} |".format(kelvin))
            print(" ----------------------------")
            print()
            break

        elif satuan == 'F':
            if suhu < 32 or suhu > 212:
                print()
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = int((5/9) * (suhu - 32))
            reamur = int((4/9) * (suhu - 32))
            kelvin = int((5/9) * (suhu - 32) + 273)
            print()
            print("Suhu", suhu ,"derajat", satuan ,"dapat dikonversi menjadi:")
            print()
            print(" ----------------------------")
            print("| SATUAN SUHU | DERAJAT SUHU |")
            print("|----------------------------|")
            print("| Celcius     | {:<12} |".format(celcius))
            print("| Reamur      | {:<12} |".format(reamur))
            print("| Kelvin      | {:<12} |".format(kelvin))
            print(" ----------------------------")
            print()
            break

        elif satuan == 'R':
            if suhu < 0 or suhu > 80: 
                print()
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = int((5/4) * suhu)
            fahrenheit = int(((9/4) * suhu) + 32)
            kelvin = int((5/4) * suhu + 273)
            print()
            print("Suhu", suhu ,"derajat", satuan ,"dapat dikonversi menjadi:")
            print()
            print(" ----------------------------")
            print("| SATUAN SUHU | DERAJAT SUHU |")
            print("|----------------------------|")
            print("| Celcius     | {:<12} |".format(celcius))
            print("| Fahrenheit  | {:<12} |".format(fahrenheit))
            print("| Kelvin      | {:<12} |".format(kelvin))
            print(" ----------------------------")
            print()
            break

        elif satuan == 'K':
            if suhu < 273 or suhu > 373:
                print()
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = suhu - 273
            fahrenheit = int((9/5) * (suhu - 273.15) + 32)
            reamur = int((4/5) * (suhu - 273))
            print()
            print("Suhu", suhu ,"derajat", satuan ,"dapat dikonversi menjadi:")
            print()
            print(" ----------------------------")
            print("| SATUAN SUHU | DERAJAT SUHU |")
            print("|----------------------------|")
            print("| Celcius     | {:<12} |".format(celcius))
            print("| Fahrenheit  | {:<12} |".format(fahrenheit))
            print("| Reamur      | {:<12} |".format(reamur))
            print(" ----------------------------")
            print()
            break

konversi(0,'')