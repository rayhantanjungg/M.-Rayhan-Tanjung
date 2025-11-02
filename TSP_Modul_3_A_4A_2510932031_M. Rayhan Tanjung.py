print('Pemesanan Tiket Bioskop')
print("" "")

pin = int(input('Masukkan pin  admin bioskop Anda : '))
while  int(input) <=3 :
    pin = int(input('Masukkan pin  admin bioskop Anda : '))
    if pin == 2031 :
        print("" "")

        while  True:
            print('Menu Film :')
            print('1. Upin Ipin')
            print('2. Film Barat')
            print('3. Boboiboy')
            print('4. Doraemon')
            print("" "")

            print('harga film 1 : Rp30000 ')
            print('harga film 2 : Rp35000')
            print('harga film 3 : Rp45000')
            print('harga film 4 : Rp60000')
            film = input('Pilih film yang ingin anda tonton : ')
            print("" "")

            if film == '1' :
                harga = 30000
                tiket = int(input('mau beli berapa tiket ? '))
                print('total bayar adalah', tiket*harga)
                
            elif film == '2' :
                harga = 35000
                tiket = int(input('mau beli berapa tiket ? '))
                print('total bayar adalah', tiket*harga)
                
            elif film == '3' :
                harga = 45000
                tiket = int(input('mau beli berapa tiket ? '))
                print('total bayar adalah', tiket*harga)
                
            elif film == '4' :
                harga = 60000
                tiket = int(input('mau beli berapa tiket ? '))
                print('total bayar adalah', tiket*harga)
                print("" "")
                
            else :
                print('pilihan tidak tersedia')
                continue
                
            lagi = input('Apakah Anda ingin melakukan transaksi lagi? (ya/tidak) ? ')
            if lagi == 'ya' :
                print("" "")
                continue
            elif lagi == 'tidak' :
                break
            else :
                print('Jawaban tidak valid')
                break

        print("" "")
        print('Terimakasih. Silahkan datang kembali.')
        quit()
    else :
        print('pin salah')

   