def konversi(suhu, satuan):
    while True:
        print("Berapa besar suhu yang ingin dikonversi?")
        suhu = int(input("Skala suhu  : "))
        print("Apakah satuan dari suhu tersebut?")
        satuan = input("Satuan suhu : ")
        satuan = satuan.upper()  # Mengonversi inputan satuan menjadi huruf kapital
        if satuan not in ['C', 'F', 'R', 'K']:
            print("Satuan suhu tidak valid. Silakan masukkan C, F, R, atau K.")
            continue

        if satuan == 'C':
            if suhu < 0 or suhu > 100:
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            fahrenheit = int(((9/5) * suhu) + 32)
            reamur = int((4/5) * suhu) 
            kelvin = int(273 + suhu)
            print()
            print("Suhu dapat dikonversi menjadi:")
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
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = int((5/9) * (suhu - 32))
            reamur = int((4/9) * (suhu - 32))
            kelvin = int((5/9) * (suhu - 32) + 273)
            print()
            print("Suhu dapat dikonversi menjadi:")
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
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = int((5/4) * suhu)
            fahrenheit = int(((9/4) * suhu) + 32)
            kelvin = int((5/4) * suhu + 273)
            print()
            print("Suhu dapat dikonversi menjadi:")
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
                print("SUHU YANG ANDA INPUTKAN TIDAK SESUAI. INPUTKAN KEMBALI!")
                continue
            celcius = suhu - 273
            fahrenheit = int((9/5) * (suhu - 273.15) + 32)
            reamur = int((4/5) * (suhu - 273))
            print()
            print("Suhu dapat dikonversi menjadi:")
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