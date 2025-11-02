print('PRAKTIKUM PROGRAMA KOMPUTER MODUL 4 : ARRAY')
print("" "")

print('Indonesia World Show')
print("" "")

NIM = int(input('Masukkan NIM : '))
XY = int(str(NIM)[8:10])
print("" "")

#Soal nomor 1
data = [{'Nama band':'One Ok Rock','Agency':'United Talent Agency (UTA)','Asal negara':'Jepang','Fee':150000,'Hit single':'Stand Out Fit In','Durasi kontrak':XY+1},
        {'Nama band':'Stray Kids','Agency':'JYP Entertainment','Asal negara':'Korea selatan','Fee':400000,'Hit single':'Maniac','Durasi kontrak':XY+2},
        {'Nama band':'.Feast','Agency':'Rusa Record','Asal negara':'Indonesia','Fee':10000,'Hit single':'Peradaban','Durasi kontrak':XY+3},
        {'Nama band':'One Direction (Reborn)','Agency':'Syco Music ','Asal negara':'Inggris','Fee':1500000,'Hit single':'What Make You Beatiful','Durasi kontrak':XY+2},
        {'Nama band':'kendrick lamar','Agency':'Wasserman Music','Asal negara':'USA','Fee':750000,'Hit single':'Humble','Durasi kontrak':XY+1}]

a=1
for i in data :
    print('data artis ke-{}'.format(a),':', i)
    a=a+1

while True:
    print("" "")
    print('Menu sistem :')
    print('Pilihan 1 = Menambahkan band')
    print('Pilihan 2 = Menghapus artis')
    print('Pilihan 3 = Mengubah fee atau durasi kontrak')
    print('Pilihan 4 = Tidak ingin mengubah apapun')
    print("" "")

#Soal nomor 2
    pilihan = int(input('Silahkan pilih menu (1/2/3/4) :'))
    if pilihan == 1 :
        Nb = input('Masukkan nama band baru : ')
        A = input('Masukkan agency band baru : ')
        An = input('Masukkan asal negara band baru : ')
        F = int(input('Masukkan fee band baru : '))
        Hs = input('Masukkan Hit single band baru : ')
        Dk = int(input('Masukkan Durasi kontrak band baru : '))
        data.append({'Nama band':Nb,'Agency':A,'Asal negara':An,'Fee':F,'Hit single':Hs,'Durasi kontrak':Dk})
        print("" "")
        continue

#Soal nomor 3
    elif pilihan == 2 :
        nbh = input('Masukkan nama band yang ingin dihapus : ')
        for i in data :
            if i['Nama band'] == nbh :
                data.remove(i)
        continue

#Soal Nomor 4
    elif pilihan == 3:
        nbhfd = input('Masukkan nama band yang ingin diganti fee atau durasi kontraknya (band yang telah dihapus tidak bisa diganti fee atau durasinya): ')
        for i in data :
            if i['Nama band'] == nbhfd :
                ganti = input('Anda ingin mengganti fee atau durasi (fee/durasi) : ')
                if ganti == 'fee':
                    i['Fee'] = int(input('Masukkan fee baru : '))
                    print("" "")

                elif ganti== 'durasi' :
                    i['Durasi kontrak'] = int(input('Masukkan durasi baru : '))
                    print("" "")
        continue
    elif pilihan == 4 :
        print("" "")
        pass
    else :
        print('Pilihan tidak tersedia')

#Soal Nomor 5
    total = 0
    for i in data:
        total += i['Fee']*i['Durasi kontrak']
    print('Total estimasi biaya seluruh band sebesar :',total)

#Soal nomor 6
    totalfee = 0
    for i in data :
        totalfee += i['Fee']
        rata2 = totalfee/len(data)
    print('Rata-rata fee dari seluruh artis sebesar :', rata2,'\n')

#Soal nomor 7
    pajaklokal = 0.08
    pajakbule = 0.18
    for i in data:
        if i['Asal negara'] == 'Indonesia':
            pbl = i['Fee']*i['Durasi kontrak']*pajaklokal
            print('Berikut adalah pendapatan bersih dari band lokal : ',i['Nama band'], pbl)

        else :
            pbb = i['Fee']*i['Durasi kontrak']*pajakbule
            print('Berikut adalah pendapatan bersih dari band bule : ',i['Nama band'], pbb,)

#Soal nomor 8
    a=1
    print("" "")
    for i in data :
        print('data artis baru ke-{}'.format(a),':', i)
        a=a+1
    break
