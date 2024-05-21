print()
print("TUGAS 8 PRAKTIKUM ALGORITMA DAN PEMOGRAMAN")
print()
print("Nama  : Salsabilla Tri Putri")
print("NIM   : 2310431017")
print("Shift : 2")
print()
def tambah(judul, penulis, penerbit, tahun, subjek, halaman):
    with open("buku.txt", "a") as file:
        file.write(f"{judul}, {penulis}, {penerbit}, {tahun}, {subjek}, {halaman}\n")
    print("\n<<<!! DATA BARU ANDA BERHASIL DITAMBAHKAN !!>>>")

def hapus(judul):
    with open("buku.txt", "r") as file:
        lines = file.readlines()
    with open("buku.txt", "w") as file:
        for line in lines:
            if not line.startswith(judul):
                file.write(line)
    print("\n<<<!! DATA LAMA ANDA BERHASIL DIHAPUSKAN !!>>>")

def tampilkan():
    with open("buku.txt", "r") as file:
        lines = file.readlines()
        if lines:
            print("Data Buku :")
            for line in lines:
                 print(line.strip())
        else:
            print("Oppss. Data buku tidak ditemukan :(")
            print("Mungkin filenya kosong T^T")
            print("Silahkan tambahkan data baru agar kami bisa menampilkan data yang kamu inginkan ^v^ ")


while True:
    print("\nLayanan kami : ")
    print("1. Menambahkan data buku baru")
    print("2. Menghapus data lama")
    print("3. Menampilkan data buku yang ada")
    print("4. Selesai")
    print()
    pilihan = input("Apa yang ingin kamu lakukan? ")
    print()
    
    if pilihan == "1":
        judul = input("Judul Buku     : ")
        penulis = input("Nama Penulis   : ")
        penerbit = input("Nama Penerbit  : ")
        tahun = input("Tahun Terbit   : ")
        subjek = input("Subjek Buku    : ")
        halaman = input("Jumlah Halaman : ")
        tambah(judul, penulis, penerbit, tahun, subjek, halaman)

    elif pilihan == "2":
        judul = input("Masukkan judul buku yang ingin dihapus : ")
        hapus(judul)

    elif pilihan == "3":
        tampilkan()

    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan kami ^v^")
        break

    else :
        print("Sepertinya pilihan kamu tidak sesuai dengan opsi manapun T^T")
        print("Berikut kami tampilkan kembali layanan-layanan yang kami sediakan. ")
print()