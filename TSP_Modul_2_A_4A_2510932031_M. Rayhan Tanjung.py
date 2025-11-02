input('nama:')
input('nim:')
input('kelompok:')
input('asisten pembimbing:')
print("" "")

print('total belanja pelanggan dan kode membership didapat dari 4 angka belakang nim (251093ABCD)')
print("" "")

A = int(input('Angka A sebagai total belanja sebanyak ='))
B = int(input('Angka B sebagai total belanja sebanyak ='))
C = int(input('Angka C sebagai total belanja sebanyak ='))
D = int(input('Angka D sebagai kode membership  ='))
print("" "")

# total belanja pelanggan
total_belanja = A*100000+B*10000+C*1000
print('total belanja pelanggan di supermarket HelloMart =', total_belanja)
print("" "")

# jenis membership pelanggan
if 1<=D<=4 :
    membership = 'silver'
    diskon     = 5/100 
    print('kode membership anda adalah' , membership)

elif 5<=D<=7 :
    membership = 'gold'
    diskon     = 1/10
    print('kode membership anda adalah' , membership)

elif D == 8 or 9 :
    membership = 'platinum'
    diskon     = 15/100
    print('kode membership anda adalah' , membership)

elif D == 0 :
    membership = 'non-member'
    diskon     = 0
    print('kode membership anda adalah' , membership)

else :
    print('maaf, pilihan anda tidak tersedia')
print("" "")

# besar diskon sesuai membership
besar_diskon = total_belanja * diskon
print('karena pelanggan memiliki membership', membership ,'maka pelanggan mendapatkan diskon sebesar', diskon ,'maka besar diskon yang diperoleh pelanggan adalah sebesar Rp',besar_diskon)
print("" "")

# total belanja setelah diskon
total_belanja_setelah_diskon = total_belanja - besar_diskon
print('total belanja pelanggan setelah mendapat diskon adalah', total_belanja_setelah_diskon)
print("" "")

# tentukan metode pembayaran
metode_pembayaran = int(input('tentukan metode pembayaran (1. tunai / 2. qris / 3. debit) :'))
print("" "")

if metode_pembayaran == 1 :
    biaya = total_belanja_setelah_diskon
    print('total biaya akhir yang harus dibayar pelanggan sebesar =', biaya)

elif metode_pembayaran == 2 :
    biaya = total_belanja_setelah_diskon + 2500
    print('total biaya akhir yang harus dibayar pelanggan sebesar =', biaya)

elif metode_pembayaran == 3 :
    biaya = total_belanja_setelah_diskon + 5000
    print('total biaya akhir yang harus dibayar pelanggan sebesar =', biaya)

else :
    print('pilihan tidak tersedia')
print("" "")

# hitung dan tampilkan total biaya akhir yang harus dibayar
total_biaya_akhir = biaya
print('total biaya akhir yang harus dibayar pelanggan adalah sebesar',biaya)
