print("TUGAS 2 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN")
nama = "Salsabila Tri Putri"
nim = "2310431017"
print("Nama : "+nama)
print("NIM  : "+nim)

print("\nBUS PT. ANS LINTAS SUMATERA")
print("\n----------------------------------")
print(" NO    TUJUAN           HARGA")
print("----------------------------------")
print(" 1.   Surabaya        Rp1.100.000")
print(" 2.   Bandung         Rp700.000")
print(" 3.   Jakarta         Rp600.000")
print(" 4.   Depok           Rp600.000")
print(" 5.   Bogor           Rp650.000")
print(" 6.   Tangerang       Rp670.000")
print()
tujuan = input("Tujuan      : ")
if (tujuan == "Surabaya") : harga = 1100000
elif (tujuan == "Bandung") : harga = 700000
elif (tujuan == "Jakarta") : harga = 600000
elif (tujuan == "Depok") : harga = 650000
elif (tujuan == "Bogor") : harga = 650000
elif (tujuan == "Tangerang") : harga = 670000
else : harga = 0

print("\n----------------------------------")
print("NO        KELAS           Biaya")
print("----------------------------------")
print("1.   Economic Class      Rp10.000")
print("2.   Business Class     Rp20.000")
print("3.   First Class         Rp30.000")
print()
kelas = input("Kelas : ")
jumlah_tiket = int(input("Jumlah tiket : "))
if (kelas == "Economic Class") : tambahan = 10000
elif (kelas == "Business Class") : tambahan = 20000
elif (kelas == "First Class") : tambahan = 30000
else : tambahan = 0
biaya_tambahan = int(tambahan*jumlah_tiket)
print()

if (jumlah_tiket>=3)&(jumlah_tiket<=5) : diskon = 5/100
elif (jumlah_tiket>5) : diskon : 10/100
else : diskon = 0

print("\n----------------------------------")
print("RINGKASAN PESANAN")
print("----------------------------------")
print("Tujuan       : "+tujuan)
print("Kelas        : "+kelas)
print("Jumlah tiket : ",jumlah_tiket)
total_biaya = int(harga*jumlah_tiket)
total = int(total_biaya+biaya_tambahan)
total_diskon = int(total*diskon)
print("Diskon       : ",total_diskon)
biaya_akhir = int(total-total_diskon)
print("Biaya akhir  : ",biaya_akhir)