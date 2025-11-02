print('Nama : M. Rayhan Tanjung')
print('NIM : 2510932031')
print('Kelompok : 4A')
print('Asisten Pembimbing : Andre Nugraha Akbar')

print('Variable yang akan digunakan ')

# 1) Nilai AB & CD 
AB=20
CD=31
# 2) Total Pemakaian
AB+CD
# 3) Biaya Energi
ben=1500
ben1=AB*ben
ben2=CD*ben
# 4) Biaya sebelum ada pajak dan administrasi
bbt=20000
bbt1=AB*bbt
bbt2=CD*bbt
totalbbt=bbt1+bbt2
# 5) Pajak totak
ppl=0.05
totalppl=ben1*ppl+ben2*ppl
# 6) Biaya administrasi
ba=0.02
totalba=ba*(ben1+ben2+totalbbt+totalppl)
# 7) Total tagihan
totaltagihan= ben1+ben2+totalbbt+totalppl+totalba

# 1)
print('Tampilkan nilai AB dan CD')
print('AB =',AB ,'dan' ' CD =',CD )

# 2)
print('Total pemakaian kWh dalam 2 bulan =', AB+CD)

# 3)
print('Biaya energi masing-masing bulan')
print('Biaya energi bulan 1 =',ben1)
print('Biaya energi bulan 2 =',ben2)

# 4)
print('Biaya selama dua bulan sebelum ada pajak dan biaya administrasi')
print('Biaya yang dikeluarkan pada bulan 1 sebelum ada pajak dan biaya administrasi =', bbt1)
print('Biaya yang dikeluarkan pada bulan 2 sebelum ada pajak dan biaya administrasi =', bbt1)
print('Total biaya yang dikeluarkan selama 2 bulan sebelum ada pajak dan biaya administrasi =', totalbbt)

# 5)
print('Pajak total kedua bulan =', totalppl)

# 6)
print('Biaya administrasi total kedua bulan ', totalba)

# 7)
print('Total tagihan pada total kedua bulan')
print('Total tagihan dari biaya yang dikeluarkan pada total kedua bulan =', totaltagihan)
