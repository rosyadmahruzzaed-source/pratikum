def hitung_nilai_akhir(tugas, uts, uas):
    return tugas * 0.3 + uts * 0.35 + uas * 0.35

def tambah_data(nilai):
    nama = input("Masukkan nama mahasiswa: ")
    if nama in nilai:
        print("Data sudah ada.")
    else:
        tugas = float(input("Nilai tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        nilai[nama] = {"tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
        print("Data berhasil ditambahkan.")

def ubah_data(nilai):
    nama = input("Masukkan nama mahasiswa yang akan diubah: ")
    if nama in nilai:
        tugas = float(input("Nilai tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        nilai[nama] = {"tugas": tugas, "uts": uts, "uas": uas, "akhir": nilai_akhir}
        print("Data berhasil diubah.")
    else:
        print("Data tidak ditemukan.")

def hapus_data(nilai):
    nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
    if nama in nilai:
        del nilai[nama]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

def tampilkan_data(nilai):
    if len(nilai) == 0:
        print("Belum ada data mahasiswa.")
        return
    print("Daftar Nilai Mahasiswa:")
    print("Nama\tTugas\tUTS\tUAS\tNilai Akhir")
    for nama, data in nilai.items():
        print(f"{nama}\t{data['tugas']}\t{data['uts']}\t{data['uas']}\t{data['akhir']:.2f}")

def cari_data(nilai):
    nama = input("Masukkan nama mahasiswa yang dicari: ")
    if nama in nilai:
        data = nilai[nama]
        print(f"Data untuk {nama}:")
        print(f"Tugas: {data['tugas']}")
        print(f"UTS: {data['uts']}")
        print(f"UAS: {data['uas']}")
        print(f"Nilai Akhir: {data['akhir']:.2f}")
    else:
        print("Data tidak ditemukan.")

def main():
    nilai = {}
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Ubah Data")
        print("3. Hapus Data")
        print("4. Tampilkan Data")
        print("5. Cari Data")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_data(nilai)
        elif pilihan == "2":
            ubah_data(nilai)
        elif pilihan == "3":
            hapus_data(nilai)
        elif pilihan == "4":
            tampilkan_data(nilai)
        elif pilihan == "5":
            cari_data(nilai)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
