import os

kaset = ["One Piece", "Naruto", "Dragon Ball", "Iron Man", "Ant Man", "Black Adam", "End Game"]
sewa = [28000, 29000, 27000, 25000, 26000, 29000, 22000]

def struk():
    print("\n========== Struk ==========")
    print("Nama Anda\t\t:", username.upper())
    print("Kaset Yang Anda Pilih\t:", kaset[pilihan-1])
    print("Uang Anda\t\t:", bayar)
    print("Kembalian\t\t:", kembalian)
    print("Terima Kasih")
    print("===========================")

loop = True

while(loop):
    os.system('cls')
    username = input("Masukan Nama Anda: ")
    print("Nama Anda\t\t:", username.upper())
    print("\nKaset Yang Tersedia\t: \n")

    for i in range(0,7):
        print(i + 1, "", kaset[i], "\t\tHarga Sewa :", sewa[i])

    print()

    pilihan = eval(input("\nMasukan Kaset Yang Ingin Disewa: "))

    try:
        if pilihan == 1:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 2:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 3:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 4:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 5:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 6:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        elif pilihan == 7:
            print("Anda Memilih\t\t:", kaset[pilihan-1])
        else :
            print("Tidak ada")

        print("Harga sewa\t\t:", sewa[pilihan-1])
    
        bayar = eval(input("Masukkan Uang Anda: "))
        print("Uang Anda\t\t:", bayar)

        while bayar < sewa[pilihan-1]:  
            outkurang = sewa[pilihan-1] - bayar 
            print("Uang Anda kurang\t:", outkurang)
            kurang = eval(input("Masukkan Uang Kembali: "))
            print("Masukkan Uang Kembali\t:", kurang)
            bayar += kurang

        kembalian = bayar - sewa[pilihan-1]

        struk()

        print("\nApakah Anda Ingin Menyewa Lagi?")
        print("1. Ya\n2. Tidak")

        pil = eval(input("Masukan Pilihan: "))

        if pil == 2:
            loop = False
            print("\nProgram Dihentikan")
            print("Terimakasih Telah Menggunakan Program Kami")

    except:
        print("Pilihan Invalid, Program Tidak Bisa Dilanjutkan")
