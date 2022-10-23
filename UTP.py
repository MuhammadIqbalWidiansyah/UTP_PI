kaset = ["One Piece", "Naruto", "Dragon Ball", "Iron Man", "Ant Man", "Black Adam", "End Game"]
sewa = [28000, 29000, 27000, 25000, 26000, 29000, 22000]

loop = True

while(loop):
  
  
        print("\nApakah Anda Ingin Menyewa Lagi ?")
        print("1. Ya\n2. Tidak")

        pil = eval(input("Masukan Pilihan : "))

        if pil == 2:
            loop = False
            print("\nProgram Dihentikan")
            print("Terimakasih Telah Menggunakan Program Kami")
        else:
            print("\nProgram Di Ulang\n")
