print("TUGAS 1 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN")
nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"
print("Nama  : "+nama)
print("NIM   : "+nim)
print("Shift : "+shift)

print("==============================================================")
print(" Mencari Luas Permukaan dan Volume Limas Segi Empat Beraturan ")
print("==============================================================")

print("A. Luas Permukaan")
import math
pjgalas = float(input("Panjang alas : "))
pjgx = pjgalas/2
print("Panjang x = ", pjgx)
tinggilimas = float(input("Tinggi limas : "))
pjgsp = math.sqrt(pjgx**2 + tinggilimas**2)
print("Panjang sisi miring = ",pjgsp)

lp = 4*((pjgalas*pjgsp)/2) + pjgalas**2
print("Luas permukaan limas segi empat beraturan =",lp)

print("B. Volume Limas")
la = pjgalas**2
volume = (la*tinggilimas)/3
print("Volume limas = ",volume)