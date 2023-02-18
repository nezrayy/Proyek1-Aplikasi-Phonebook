import os


def tambah():
    os.system('cls')
    tmb = open("kontak.txt", 'a')
    tempNama = input("Masukkan nama: ")
    tempNomor = input("Masukkan nomor: ")
    tmb.write("{}\n".format(tempNama + "\t\t" + tempNomor))
    tmb.close()
    print("Kontak baru sudah berhasil ditambahkan!")


def tampilKontak():
    if os.path.getsize("kontak.txt") == 0:
        print("Daftar kontak kosong!")
    else:
        os.system('cls')
        tmp = open("kontak.txt", 'r')
        print("Nama\t\tNomor\n=========================\n" + tmp.read())
        # print(tmp.read())
        tmp.close()


def hapus():
    if os.path.getsize("kontak.txt") == 0:
        print("Daftar kontak kosong!")
    else:
        tampilKontak()
        with open("kontak.txt", 'r') as cek:
            isi = cek.read()
            kontakDihapus = input("Masukkan nama yang akan dihapus: ")
        if kontakDihapus in isi:
            with open("kontak.txt", 'r') as hps:
                lines = hps.readlines()
            isiBaru = [line for line in lines if kontakDihapus not in line]
            with open("kontak.txt", 'w') as hps:
                hps.writelines(isiBaru)
            print("Kontak berhasil dihapus!")
        else:
            os.system('cls')
            print(
                "Kontak tidak tersedia, silahkan pilih nama yang tersedia pada daftar anda.")

def editKontak():
    os.system('cls')
    if os.path.getsize("kontak.txt") == 0:
        print("Daftar kontak kosong!")
    else:
        tampilKontak()
        namaDiganti = input("Masukan nama yang diganti: ")
        namaTemp = input("Masukan nama baru: ")
        nomorTemp = input("Masukan nomor baru: ")
        with open("kontak.txt", 'r') as edit:
            lines = edit.readlines()
        with open("kontak.txt", 'w') as edit:
            for index, line in enumerate(lines):
                if namaDiganti in line:
                    lines[index] = namaTemp + "\t\t" + nomorTemp + '\n'
            edit.writelines(lines)
            print("Kontak berhasil diubah!")


def cari():
    if os.path.getsize("kontak.txt") == 0:
        print("Daftar kontak kosong!")
    else:
        namaDicari = input("Cek nama : ")
        with open("kontak.txt", 'r') as cr:
            for line in cr:
                if namaDicari in line:
                    ada = True
                else:
                    ada = False
            if ada == True:
                os.system('cls')
                print("Nama\t\tNomor\n=========================\n" + line.strip())
            else:
                print("Kontak tidak tersedia")


# Main
while True:
    try:
        os.system('cls')
        pilih = int(input(
            ".:*{ Phonebook-mu }*:.\n\n1. Buat Kontak Baru\n2. Hapus Kontak\n3. Cari kontak\n4. Edit Kontak\n5. Daftar Kontak\n6. Keluar\n\nPilih: "))
        if pilih == 1:
            tambah()
            input()
        elif pilih == 2:
            hapus()
            input()
        elif pilih == 3:
            cari()
            input()
        elif pilih == 4:
            editKontak()
            input()
        elif pilih == 5:
            tampilKontak()
            input()
        elif pilih == 6:
            exit()
        else:
            print("Pilihan tidak sesuai! Ulangi.")
            input()
    except Exception:
        print("Pilihan tidak sesuai! Ulangi.")
# endMain
