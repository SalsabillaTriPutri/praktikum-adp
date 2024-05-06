nama = "Salsabilla Tri Putri"
nim = "2310431017"
shift = "2"
print()
print(" TUGAS ke 6 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN\n")
print(" Materi : ARRAY 2D")
print(" Nama   : "+nama)
print(" NIM    : "+nim)
print(" Shift  : "+shift)
print()

n = int(input("  Banyak mahasiswa   : "))

nama_mahasiswa = []
for i in range(n):
    nama = input("     Nama mahasiswa ke-"+str(i+1)+" : ")
    nama_mahasiswa.append(nama)
print("     List nama mahasiswa : ",nama_mahasiswa)


m = int(input("\n  Jumlah mata kuliah : " ))

mata_kuliah = []
for i in range(m):
    matkul = input("     Mata kuliah ke-"+str(i+1)+" : ")
    mata_kuliah.append(matkul)
print("     List mata kuliah : ",mata_kuliah)


print()
print("  Nilai mahasiswa per mata kuliah : ")
nilai_ujian = []
for i in range(n):
    nilai_mahasiswa = []
    for j in range(m):
        nilai = int(input("     Nilai mata kuliah "+str(j+1)+" "+nama_mahasiswa[i]+" : "))
        nilai_mahasiswa.append(nilai)
    nilai_ujian.append(nilai_mahasiswa)
print("     List nilai ujian mahasiswa : ",nilai_ujian)


print("\n  Tabel Nilai Ujian Mahasiswa :")
print("     ""{:<10}".format(""), end=" ")
for mk in mata_kuliah:
    print("     ""{:<10}".format(mk), end=" ")
print()
for i in range(n):
    print("     ""{:<10}".format(nama_mahasiswa[i]), end=" ")
    for j in range(m):
        print("     ""{:<10}".format(nilai_ujian[i][j]), end=" ")
    print()

print("\n  Rata=rata Nilai Setiap Mahasiswa : ")
rata_rata = []
for nilai_mahasiswa in nilai_ujian:
    rata = int(sum(nilai_mahasiswa)/m)
    rata_rata.append(rata)
for i in range(n):
    print("     Rata-rata nilai ujian ",nama_mahasiswa[i]," : ",rata_rata[i])


print("\n  Nilai tertinggi dan terendah masing-masing mata kuliah :")
for j in range(m):
    nilai_matkul = [nilai[j] for nilai in nilai_ujian]
    nilai_tertinggi = max(nilai_matkul)
    nilai_terendah = min(nilai_matkul)
    for i in range(n):
        if nilai_matkul[i] == nilai_tertinggi:
            mahasiswa_tertinggi = [nama_mahasiswa[i]]
        if nilai_matkul[i] == nilai_terendah:
            mahasiswa_terendah = [nama_mahasiswa[i]]
    
    print("     Nilai tertinggi di mata kuliah ",mata_kuliah[j]," adalah ", nilai_tertinggi)
    print("     Mahasiswa dengan nilai tertingi adalah ", mahasiswa_tertinggi)
    print("     Nilai terendah di mata kuliah ",mata_kuliah[j]," adalah ", nilai_terendah)
    print("     Mahasiswa dengan nilai terendah adalah ", mahasiswa_terendah)
print()