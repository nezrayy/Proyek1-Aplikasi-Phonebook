import os
import fileinput
import sys


def tambah():
    os.system('cls')
    tmb = open("kontak.txt", "a")
    tempNama = input("Masukkan nama: ")
    tempNomor = input("Masukkan nomor: ")
    tmb.write("{}\n".format(tempNama + "\t\t" + tempNomor))
    tmb.close()
    print("Kontak baru sudah berhasil ditambahkan!")
    input()


def tampilKontak():
    if os.path.getsize('kontak.txt') == 0:
        print("Daftar kontak kosong!")
    else:
        os.system('cls')
        tmp = open("kontak.txt", "r")
        print("Nama\t\tNomor\n=========================")
        print(tmp.read())
        tmp.close()


def hapus():
    if os.path.getsize('kontak.txt') == 0:
        print("Daftar kontak kosong!")
    else:
        kontakDihapus = input("Masukkan nama yang akan dihapus: ")
        with open('kontak.txt', 'r') as f:
            lines = f.readlines()
        isiBaru = [line for line in lines if kontakDihapus not in line]
        with open('kontak.txt', 'w') as f:
            f.writelines(isiBaru)
        print("Kontak berhasil dihapus!")


def edit():
    if os.path.getsize('kontak.txt') == 0:
        print("Daftar kontak kosong!")
    else:
        namaDiedit = input("Masukkan nama yang akan diedit: ")
        tempNamaBaru = input("Masukkan nama baru: ")
        tempNomorBaru = input("Masukkan nomor baru: ")
        for line in fileinput.input("kontak.txt", inplace=1):
            if namaDiedit in line:
                line = line.replace(line, tempNamaBaru +
                                    "\t\t" + tempNomorBaru + "\n")
                sys.stdout.write(line)
        print("Kontak berhasil diedit!")


def cari():
    if os.path.getsize('kontak.txt') == 0:
        print("Daftar kontak kosong!")
    else:
        with open('kontak.txt', 'r') as file:
            # read all content of a file
            isi = file.read()
            # check if string present in a file
            namaDicari = input("Cek nama : ")
            if namaDicari in isi:
                print("Kontak tersedia")
            else:
                print("Kontak tidak tersedia")


# Main
while True:
    try:
            os.system('cls')
            pilih = int(input("  Phonebook-mu\n\n1. Buat Kontak Baru\n2. Hapus Kontak\n3. Cari kontak\n4. Edit Kontak\n5. Daftar Kontak\n6. Keluar\nPilih: "))
            if pilih == 1:
                tambah()
            elif pilih == 2:
                tampilKontak()
                hapus()
                input()
            elif pilih == 3:
                cari()
                input()
            elif pilih == 4:
                tampilKontak()
                edit()
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
