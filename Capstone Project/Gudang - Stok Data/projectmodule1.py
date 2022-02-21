# Data Initialization
product = [{'Kode Barang' : 'A1', 'Jenis Barang' : 'Pulpen', 'Stok Awal' : 20, 'Stok IN' : 0, 'Stok OUT' : 0, 'Stok Akhir' : 20},
{'Kode Barang' : 'A2', 'Jenis Barang' : 'Buku', 'Stok Awal' : 10, 'Stok IN' : 0, 'Stok OUT' : 0, 'Stok Akhir' : 10}]

# Read Data Function
def read_stock():
    read = True
    while read != '3':
        print('''
        Report Stok Barang

    1. Report Seluruh Stok Barang
    2. Report Stok Barang Tertentu
    3. Kembali Ke Menu Utama
    ''')
        read = input('Silahkan Pilih Sub Menu Report Stok Barang (1-3) : ')
        if read == '1':
            if len(product) != 0:
                print('\n\tDaftar Stok Barang\n')
                for j, i in enumerate(product):
                    print(f"{j+1}, Kode Barang : {i['Kode Barang']}, Jenis Barang : {i['Jenis Barang']}, Stok Awal : {i['Stok Awal']}, Stok IN : {i['Stok IN']}, Stok OUT : {i['Stok OUT']}, Stok Akhir : {i['Stok Akhir']}")
            else:
                print('\n-----Tidak ada Daftar Stok Barang-----')
        elif read == '2':
            if len(product) != 0:
                prd = input('Masukkan Kode Barang : ').upper()
                print(f'\nStok Barang dengan Kode Barang : {prd}')
                for j, i in enumerate(product):
                    if i['Kode Barang'] == prd:
                        print(f"\n{j+1}, Kode Barang : {i['Kode Barang']}, Jenis Barang : {i['Jenis Barang']}, Stok Awal : {i['Stok Awal']}, Stok IN : {i['Stok IN']}, Stok OUT : {i['Stok OUT']}, Stok Akhir : {i['Stok Akhir']}")
                        break
                else:
                    print('-----Kode Barang Tidak Ada-----')
            else:
                print('\n-----Tidak ada Daftar Stok Barang-----')
        elif read == '3':
            break
        else:
            print('\n-----Pilihan Sub Menu Tidak Ada-----')

# Create Data Function
def create_stock():
    create = True
    while create != '2':
        print('''
        Menambahkan Stok Barang

    1. Tambah Stok Barang
    2. Kembali ke Menu Utama
    ''')
        create = input('Silahkan Pilih Sub Menu Create (1-2) : ')
        if create == '1':
            prdCode = input('Masukkan Kode Barang : ').upper()
            for j, i in enumerate(product):
                if prdCode == i['Kode Barang']:
                    print('\n-----Daftar Kode Barang Sudah Ada-----')
                    break
            else:
                prdJenis = input('Masukkan Jenis Barang : ').capitalize()
                for j, i in enumerate(product):
                    if prdJenis == i['Jenis Barang']:
                        print('-----Jenis Barang {} Sudah Ada Dengan Kode Barang {}-----'.format(prdJenis, i['Kode Barang']))
                        break
                else:
                    prdStokAwal = int(input('Masukkan Jumlah Stok Awal : '))
                    prdStokIn = int(input('Masukkan Jumlah Stok IN : '))
                    prdStokOut = int(input('Masukkan Jumlah Stok OUT : '))
                    while True:
                        saveData = input('Apakah sudah yakin untuk menyimpan data ? (Yes/No) : ').capitalize()
                        if saveData == 'Yes':
                            product.append({'Kode Barang' : (prdCode), 'Jenis Barang' : (prdJenis), 'Stok Awal' : (prdStokAwal), 'Stok IN' : (prdStokIn), 'Stok OUT' : (prdStokOut), 'Stok Akhir' : (prdStokAwal+prdStokIn-prdStokOut)})
                            print('\n-----Data Berhasil Disimpan-----')
                            break
                        elif saveData == 'No':
                            print('\n-----Data Tidak Disimpan-----')
                            break
                        else:
                            print('\n-----Format Penulisan Salah-----')
        elif create == '2':
            break
        else:
            print('\n-----Pilihan Sub Menu Tidak Ada-----')

# Delete Data Function
def delete_stock():
    delete = True
    while delete != '2':
        print('''
        Menghapus Stok Barang

    1. Menghapus Stok Barang
    2. Kembali Ke Menu Utama
    ''')
        delete = input('Silahkan Pilih Sub Menu Delete (1-2) : ')
        if delete == '1':
            inputDel = input('Masukkan Kode Barang yang ingin dihapus : ').upper()
            for j, i in enumerate(product):
                if inputDel == i['Kode Barang']:
                    print(f"""
                    -----Stok Barang Tersedia-----\n
                    {j+1}, Kode Barang : {i['Kode Barang']}, Jenis Barang : {i['Jenis Barang']}, Stok Awal : {i['Stok Awal']}, Stok IN : {i['Stok IN']}, Stok OUT : {i['Stok OUT']}, Stok Akhir : {i['Stok Akhir']}\n
                    -----Data Tersebut Akan Dihapus-----
                    """)
                    while True:
                        saveDel = input('Apakah yakin ingin menghapus stok barang tersebut ? (Yes/No) : ').capitalize()
                        if saveDel == 'Yes':
                            for i in range(len(product)):
                                if product[i]['Kode Barang'] == inputDel:
                                    del product[i]
                                    print('\n-----Data Berhasil Dihapus-----')
                                    break
                            break
                        elif saveDel == 'No':
                            print('\n-----Data Tidak Terhapus-----')
                            break
                        else:
                            print('\n-----Format Penulisan Salah-----')
                    break
            else:
                print('\n-----Daftar Kode Barang Tidak Tersedia-----')
        elif delete == '2':
            break
        else:
            print('\n-----Pilihan Sub Menu Tidak Ada-----')
            
        
# Update Data Function
def update_stock():
    update = True
    while update != '2':
        print('''
        Update Stok Barang

    1. Update Stok Barang
    2. Kembali Ke Menu Utama
    ''')
        update = input('Silahkan Pilih Sub Menu Update (1-2) : ')
        if update == '1':
            inputUpdate = input('Masukkan Kode Barang yang ingin di update : ').upper()
            for j, i in enumerate(product):
                if inputUpdate == i['Kode Barang']:
                    print(f"""
                    -----Data Stok Barang Dengan Kode Barang {inputUpdate}-----\n
                    {j+1}, 'Kode Barang' : {i['Kode Barang']}, 'Jenis Barang' : {i['Jenis Barang']}, Stok Awal : {i['Stok Awal']}, Stok IN : {i['Stok IN']}, Stok OUT : {i['Stok OUT']}, Stok Akhir : {i['Stok Akhir']}\n
                    -----Data Tersebut Akan di Update-----
                    """)
                    while True:
                        askUpdate = input('Apakah ingin melanjutkan update ? (Yes/No) : ').capitalize()
                        if askUpdate == 'Yes':
                            colUpdate = input('Pilih Kolom Yang Ingin di Update : ').capitalize()
                            if colUpdate == 'Kode barang':
                                newKodeBarang = input('Masukkan Kode Barang Baru : ').upper()
                                while True:
                                    askSave = input('Apakah Sudah Yakin Untuk Mengubah Data ? (Yes/No) : ').capitalize()
                                    if askSave == 'Yes':
                                        for j, i in enumerate(product):
                                            if newKodeBarang == i['Kode Barang']:
                                                print('\n-----Kode Barang {} Sudah Ada-----'.format(i['Kode Barang']))
                                                break
                                        else:
                                            for j, i in enumerate(product):
                                                if inputUpdate == i['Kode Barang']:
                                                    i['Kode Barang'] = newKodeBarang
                                                    print('\n-----Data Berhasil di Update-----')
                                                    break
                                        break
                                    elif askSave == 'No':
                                        print('\n-----Data Tidak di Update-----')
                                        break
                                    else:
                                        print('\n-----Format Penulisan Salah-----')
                            elif colUpdate == 'Jenis barang':
                                newJenisBarang = input('Masukkan Jenis Barang Baru : ').capitalize()
                                while True:
                                    askSave = input('Apakah Sudah Yakin Untuk Mengubah Data ? (Yes/No) : ').capitalize()
                                    if askSave == 'Yes':
                                        for j, i in enumerate(product):
                                            if newJenisBarang == i['Jenis Barang']:
                                                print('\n-----Jenis Barang {} Sudah Ada-----'.format(i['Jenis Barang']))
                                                break
                                        else:
                                            for j, i in enumerate(product):
                                                if inputUpdate == i['Kode Barang']:
                                                    i['Jenis Barang'] = newJenisBarang
                                                    print('\n-----Data Berhasil di Update-----')
                                                    break
                                        break
                                    elif askSave == 'No':
                                        print('\n-----Data Tidak di Update-----')
                                        break
                                    else:
                                        print('\n-----Format Penulisan Salah-----')
                            elif colUpdate == 'Stok awal':
                                newStokAwal = int(input('Masukkan Jumlah Stok Awal : '))
                                while True:
                                    askSave = input('Apakah Sudah Yakin Untuk Mengubah Data ? (Yes/No) : ').capitalize()
                                    if askSave == 'Yes':
                                        i['Stok Awal'] = newStokAwal
                                        i['Stok Akhir'] = i['Stok Awal'] + i['Stok IN'] - i['Stok OUT']
                                        print('\n-----Data Berhasil di Update-----')
                                        break
                                    elif askSave == 'No':
                                        print('\n-----Data Tidak di Update-----')
                                        break
                                    else:
                                        print('\n-----Format Penulisan Salah-----')
                            elif colUpdate == 'Stok in':
                                newStokIn = int(input('Masukkan Jumlah Stok IN : '))
                                while True:
                                    askSave = input('Apakah Sudah Yakin Untuk Mengubah Data ? (Yes/No) : ').capitalize()
                                    if askSave == 'Yes':
                                        i['Stok IN'] = newStokIn
                                        i['Stok Akhir'] = i['Stok Awal'] + i['Stok IN'] - i['Stok OUT']
                                        print('\n-----Data Berhasil di Update-----')
                                        break
                                    elif askSave == 'No':
                                        print('\n-----Data Tidak di Update-----')
                                        break
                                    else:
                                        print('\n-----Format Penulisan Salah-----')
                            elif colUpdate == 'Stok out':
                                newStokOut = int(input('Masukkan Jumlah Stok OUT : '))
                                while True:
                                    askSave = input('Apakah Sudah Yakin Untuk Mengubah Data ? (Yes/No) : ').capitalize()
                                    if askSave == 'Yes':
                                        i['Stok OUT'] = newStokOut
                                        i['Stok Akhir'] = i['Stok Awal'] + i['Stok IN'] - i['Stok OUT']
                                        print('\n-----Data Berhasil di Update-----')
                                        break
                                    elif askSave == 'No':
                                        print('\n-----Data Tidak di Update-----')
                                        break
                                    else:
                                        print('\n-----Format Penulisan Salah-----')
                            else:
                                print('\n-----Format Penulisan Salah-----')
                                break
                        elif askUpdate == 'No':
                            break
                        else:
                            print('\n-----Format Penulisan Salah-----')
                        break
                    break
            else:
                print('\n-----Kode Barang {} Tidak Ada-----'.format(inputUpdate))
        elif update == '2':
            break
        else:
            print('\n-----Pilihan Sub Menu Tidak Ada-----')
                

# Main Menu
while True:
    print('''
        Stok Data Gudang Purwadhika

    1. Report Stok Barang
    2. Menambahkan Stok Barang
    3. Menghapus Stok Barang
    4. Update Stok Barang
    5. Exit Program
    ''')

    inputUser = input('Pilih menu : ')
    if inputUser == '1':
        read_stock()
    elif inputUser == '2':
        create_stock()
    elif inputUser == '3':
        delete_stock()
    elif inputUser == '4':
        update_stock()
    elif inputUser == '5':
        break
    else:
        print('\n-----Pilihan Menu Tidak Ada-----')