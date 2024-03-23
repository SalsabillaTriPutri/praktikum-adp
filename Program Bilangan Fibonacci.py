nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"

print("\nTUGAS 3 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN")
print("Nama  : "+nama)
print("NIM   : "+nim)
print("Shift : "+shift)
print("\n=====================================")
print("      PROGRAM BILANGAN FIBONACCI     ")
print("=====================================\n")

while True:
    n = int(input("Masukkan nilai n : "))
    if n in range(3, 101) or n in range(110, 200):
        f1, f2 = 1, 1
        hasil = 0
        for i in range(n):
            hasil += f1
            f1, f2 = f2, f1 + f2
        print("Bilangan fibonacci ke",n," adalah : ", f1)
        print("Hasil penjumlahan bilangan fibonacci dari f1 sampai f",n,"adalah =", hasil)
        break
    else:
        print("Nilai n tidak masuk dalam interval. Masukkan lagi!")
print( )