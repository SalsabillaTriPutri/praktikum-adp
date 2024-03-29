nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"

print("\nNama  : "+nama)
print("NIM   : "+nim)
print("Shift : "+shift)

print("\n============================")
print("     PROGRAM LIRIK LAGU     ")
print("============================\n")
singer = input("Song by : ")
title = input("Title   : ")
vokal = 'aiueoAIUO'
lirik = input("\nLirik : ")
perubahan = ''

for huruf in lirik:
    if huruf in vokal:
        perubahan += "i"
    else:
        perubahan += huruf

print("Lirik yang telah dirobah : ",perubahan)
print()
