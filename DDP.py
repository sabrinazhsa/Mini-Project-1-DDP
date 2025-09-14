print("Sabrina Azhmalia Nisa")
print("NIM 2509116051")
print("Ssitem Informasi B")

# Daftar Resep Masakan yang Tersedia
Resep = ["Cireng", "Pisang_Keju"]
print(Resep)


while True:
    print("=== Resep Masakan Simple ===")
    print("1. Ubah Resep")
    print("2. Lihat Resep")
    print("3. Hapus Resep")
    print("4. Keluar")

    choice = input("Pilih 1/2/3/4: ")

    if choice == "1":
        Nama = input("Apakah anda ingin mengupdate resep?: (ya/tidak)")
        if Nama == "ya":
            print("Memperbarui nama resep!")
            Nama_Lama = input("Masukkan nama resep yang ingin diupdate: ")
            if Nama_Lama in Resep:
                Nama_Baru = input("Masukkan nama baru yang ingin dipakai: ")
                Resep.remove(Nama_Lama)
                Resep.append(Nama_Baru)
                print("Resep", Nama_Lama, "telah diubah menjadi", Nama_Baru)
        if Nama == "tidak":
            print("Baiklah!")
        else:
            print("silakan coba lagi!")
    elif choice == "2":
        print("Daftar Resep", Resep)
        Nama = input("Masukkan resep: ")
        if Nama == "Cireng":
            print("\nBahan: Tepung tapioka, tepung terigu, garam, air panas")
            print("\nCara: Campur semua bahan, bentuk adonan sesuai selera, goreng diminyak panas, cireng siap dinikmati")
        elif Nama == "Pisang_Keju":
            print("\nBahan: Buah pisang, keju, susu kental manis, gula palem")
            print("\nCara: Kupas buah pisang dan belah jadi beberapa bagian, taburi keju parut, susu kental manis, gula palem, pisang keju siap dinikmati")
        else:
            print("Resep tidak ada!")
    elif choice == "3":
        Hapus = input("Masukkan resep yang ingin dihapus: (Cireng, Pisang_Keju)" )
        if Hapus in Resep:
            Resep.remove(Hapus)
            print(f"Resep sudah terhapus!")
        else:
            print("Resep tidak ada!")
    elif choice == "4":
        print("Terima kasih, have a nice day!")
        break
    else:
        print("Tidak valid!")


