
nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"
print()
print("TUGAS 5 PRAKTIKUM ADP\n")
print("Materi : ARRAY")
print("Nama   : "+nama)
print("NIM    : "+nim)
print("Shift  : "+shift)

print()
import math
while True:
    n = int(input("Banyak data : "))

    x = [0] * n
    fx = [0] * n
    gx = [0] * n
    hx = [0] * n

    for i in range(n):
        x[i] = int(input(f"Nilai x ke-{i+1} : "))
        if x[i] > 0:
            fx[i] = int(3*x[i]**2 + 7*x[i] - 2)
        elif x[i] < 0:
            fx[i] = int(2*x[i]**2 - 5*x[i] - 4)
        else:
            fx[i] = 0
        gx[i] = int(fx[i]**2 - math.sqrt(fx[i]))
        hx[i] = int(fx[i] * gx[i])

    print("\n --------------------------------------------------")
    print("|                   TABEL HASIL                    |")
    print("|--------------------------------------------------|")
    print("|    x    |    f(x)    |    g(x)    |     h(x)     |")
    print("|--------------------------------------------------|")
    for i in range(n):
        print(f"|    {x[i]}   |     {fx[i]}    |   {gx[i]}   |   {hx[i]}  |")
    print(" -------------------------------------------------- ")
    print()
    pilihan = input("Apakah Anda ingin kembali memasukkan nilai x ? (Y/N): ")
    if pilihan.upper() != 'Y':
        break
