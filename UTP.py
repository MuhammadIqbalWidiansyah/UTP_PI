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
    
    
    try:
  
  
        print("\nApakah Anda Ingin Menyewa Lagi ?")
        print("1. Ya\n2. Tidak")

        pil = eval(input("Masukan Pilihan : "))

        if pil == 2:
            loop = False
            print("\nProgram Dihentikan")
            print("Terimakasih Telah Menggunakan Program Kami")
        else:
            print("\nProgram Di Ulang\n")
    except:
        print("Pilihan Invalid, Program Tidak Bisa Dilanjutkan")
