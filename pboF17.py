import sqlite3
up=sqlite3.connect('c:/sqlite/sewaHotel.db')
cursor=up.cursor()

class DataManager:
    def __init__(self):
        self.up=sqlite3.connect('c:/sqlite/sewaHotel.db')
        self.cursor=self.up.cursor()
    def executeQuery(self,query):
        self.cursor.execute(query)
        all_results=self.cursor.fetchall()
        self.up.commit()
        return all_results

class Kamar(DataManager):
    def getDaftarKamar(self):
        showKamar=self.executeQuery('SELECT * FROM tipeKamar')
        print("IDKamar \t Tipe Kamar \t Fasilitas \t Harga Kamar")
        for row in showKamar:
            print(row[0],'\t\t',row[1],'\t\t',row[2],'\t',row[3])

class Fasilitas(DataManager):
    def getDaftarFasilitas(self):
        showFasilitas=self.executeQuery('SELECT * FROM fasilitasTambahan')
        print("IDFasilitas \t Jenis Fasilitas \t Keterangan \t Biaya Tambahan")
        for row in showFasilitas:
            print(row[0],'\t\t',row[1],'\t\t',row[2],'\t',row[3])

class Administrator(DataManager):
    def getDaftarAdministrator(self):
        showAdministrator=self.executeQuery('SELECT * FROM administrator')
        print("IDAdmin \t Nama Admin \t Contact")
        for row in showAdministrator:
            print(row[0],'\t\t',row[1],'\t\t',row[2])

class Customer(DataManager):  
    def setDataCustomer(self):
        nik = str(input('NIK:'))
        name = str(input('Nama:'))
        alamat = str(input('Alamat:'))
        nomer = str(input('No Telpon:'))
        email = str(input('Email:'))
        sandi = str(input('Sandi:'))
        self.query='INSERT INTO customers (NIK,NamaCustomer,Alamat,NoTelp,Email,Sandi) VALUES ( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');'
        self.query=self.query % (nik,name,alamat,nomer,email,sandi)
        self.executeQuery(self.query)

run=True
def tampilkanMenu():
    print('\n','##############  SELAMAT DATANG DI PROGRAM BOOKING HOTEL PBO  ##############','\n')
    print('     ---MENU---','\n','1. Pilihan Kamar','\n','2. Fasilitas Tambahan','\n','3. Administrator','\n','4. Booking Hotel','\n','5. Exit')
    menu=int(input('Masukkan Pilihan Menu:'))
    return menu

class klompok(DataManager):
    def lanjutan(self):
        pilih3=int(input('Berapa Hari Anda Akan Menyewa: ' ))
        Fasilitas().getDaftarFasilitas()
        pilih2=int(input('Masukkan IDFasilitas Pilihan Anda: ' ))
        if pilih2==4001:
            self.query = 'SELECT t.IDKamar, t.HargaKamar, f.IDFasilitas, f.BiayaTambahan, (f.BiayaTambahan+(t.HargaKamar*\'%s\')) as total from tipeKamar t join fasilitasTambahan f where IDKamar = \'%s\' and IDFasilitas =\'%s\''
            self.query=self.query % (pilih3,pilih,pilih2)
            transaksi=self.executeQuery(self.query)
            print("IDKamar \t Harga Kamar \t IDFasilitas \t Biaya Tambahan \t Total")
            for row in transaksi :
                print(row[0],'\t\t',row[1],'\t',row[2],'\t\t',row[3],'\t\t',row[4])
        elif pilih2==4002:
            self.query = 'SELECT t.IDKamar, t.HargaKamar, f.IDFasilitas, f.BiayaTambahan, (f.BiayaTambahan+(t.HargaKamar*\'%s\')) as total from tipeKamar t join fasilitasTambahan f where IDKamar = \'%s\' and IDFasilitas =\'%s\''
            self.query=self.query % (pilih3,pilih,pilih2)
            transaksi=self.executeQuery(self.query)
            print("IDKamar \t Harga Kamar \t IDFasilitas \t Biaya Tambahan \t Total")
            for row in transaksi :
                print(row[0],'\t\t',row[1],'\t',row[2],'\t\t',row[3],'\t\t',row[4]) 
        elif pilih2==4003:
            self.query = 'SELECT t.IDKamar, t.HargaKamar, f.IDFasilitas, f.BiayaTambahan, (f.BiayaTambahan+(t.HargaKamar*\'%s\')) as total from tipeKamar t join fasilitasTambahan f where IDKamar = \'%s\' and IDFasilitas =\'%s\''
            self.query=self.query % (pilih3,pilih,pilih2)
            transaksi=self.executeQuery(self.query)
            print("IDKamar \t Harga Kamar \t IDFasilitas \t Biaya Tambahan \t Total")
            for row in transaksi :
                print(row[0],'\t\t',row[1],'\t',row[2],'\t\t',row[3],'\t\t',row[4])
        elif pilih2==4004:
            self.query = 'SELECT t.IDKamar, t.HargaKamar, f.IDFasilitas, f.BiayaTambahan, (f.BiayaTambahan+(t.HargaKamar*\'%s\')) as total from tipeKamar t join fasilitasTambahan f where IDKamar = \'%s\' and IDFasilitas =\'%s\''
            self.query=self.query % (pilih3,pilih,pilih2)
            transaksi=self.executeQuery(self.query)
            print("IDKamar \t Harga Kamar \t IDFasilitas \t Biaya Tambahan \t Total")
            for row in transaksi :
                print(row[0],'\t\t',row[1],'\t',row[2],'\t\t',row[3],'\t\t',row[4])
        elif pilih2==4005:
            self.query = 'SELECT t.IDKamar, t.HargaKamar, f.IDFasilitas, f.BiayaTambahan, (f.BiayaTambahan+(t.HargaKamar*\'%s\')) as total from tipeKamar t join fasilitasTambahan f where IDKamar = \'%s\' and IDFasilitas =\'%s\''
            self.query=self.query % (pilih3,pilih,pilih2)
            transaksi=self.executeQuery(self.query)
            print("IDKamar \t Harga Kamar \t IDFasilitas \t Biaya Tambahan \t Total")
            for row in transaksi :
                print(row[0],'\t\t',row[1],'\t',row[2],'\t\t',row[3],'\t\t',row[4])
        else:
            print('Pilihan Tidak Tersedia')

while run:
    menu=tampilkanMenu()
    if menu==1:
        Kamar().getDaftarKamar()
    elif menu==2:
        Fasilitas().getDaftarFasilitas()
    elif menu==3:
        Administrator().getDaftarAdministrator()
    elif menu==4:
        print('Lengkapi Data Diri Anda')
        Customer().setDataCustomer()
        Kamar().getDaftarKamar()
        pilih=int(input('Masukkan IDKamar Pilihan Anda: ' ))
        if pilih==3001:
            klompok().lanjutan()
        elif pilih==3002:
            klompok().lanjutan()
        elif pilih==3003:
            klompok().lanjutan()
        elif pilih==3004:
            klompok().lanjutan()
        elif pilih==3005:
            klompok().lanjutan()
        elif pilih==3006:
            klompok().lanjutan()
        else:
            print('Pilihan Tidak Tersedia')
    elif menu==5:
        exit()
    else:
        print('Pilihan Tidak Tersedia')








tampilkanMenu()