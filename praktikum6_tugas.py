import os

mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'uts':0,
    'uas':0,
    'tugas':0,
    'nilai_akhir':0
}

data_mahasiswa = {}

mahasiswa = dict.fromkeys(mahasiswa_template.keys())

def tambah_data():
    print("Silahkan isi data di bawah ini,")
    # mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("Nama           : ")
    mahasiswa['nim'] = int(input("NIM            : "))
    mahasiswa['uts'] = int(input("Nilai UTS      : "))
    mahasiswa['uas'] = int(input("Nilai UAS      : "))
    mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
    NAMA = mahasiswa['nama']
    NIM = mahasiswa['nim']
    UTS = mahasiswa['uts']
    UAS = mahasiswa['uas']
    TUGAS = mahasiswa['tugas']
    mahasiswa['nilai_akhir'] = TUGAS*0.30 + UTS*0.35 + UAS*0.35
    NILAI_AKHIR = mahasiswa['nilai_akhir']

    KEY = mahasiswa['nim']
    data_mahasiswa.update({KEY:mahasiswa})
    print(data_mahasiswa)

    print("-"*70)
    print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
    print("="*70)
    print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
    print("-"*70)

    is_done()

def lihat_data():
    print("-"*70)
    print(f"|{'DAFTAR MAHASISWA':^68}|")
    print("-"*70)
    print(f"|{'No':^4}|{'Nama':^15}|{'NIM':^10}|{'UTS':^7}|{'UAS':^7}|{'Tugas':^7}|{'Nilai Akhir':^12}|")
    print("="*70)
    print(f"|{'Mohon maaf, fitur ini belum tersedia, mau tanya dosen dulu.':^68}|")
    
    # for mahasiswa in data_mahasiswa.items():
    #         print(f"|{no:^4}|{NAMA:^15}|{KEY:^10}|{UTS:^7}|{UAS:^7}|{TUGAS:^7}|{NILAI_AKHIR:^12.2f}|")            
    #         no += 1

    is_done()

def ubah_data():
    print("Silahkan masukkan NIM yang akan di ubah datanya,")
    nim = int(input("NIM            : "))
    if nim in data_mahasiswa.keys():
        mahasiswa['uts'] = int(input("Nilai UTS      : "))
        mahasiswa['uas'] = int(input("Nilai UAS      : "))
        mahasiswa['tugas'] = int(input("Nilai Tugas    : "))
        NAMA = mahasiswa['nama']
        NIM = mahasiswa['nim']
        UTS = mahasiswa['uts']
        UAS = mahasiswa['uas']
        TUGAS = mahasiswa['tugas']
        mahasiswa['nilai_akhir'] = TUGAS*0.30 + UTS*0.35 + UAS*0.35
        NILAI_AKHIR = mahasiswa['nilai_akhir']

        KEY = mahasiswa['nim']
        data_mahasiswa.update({KEY:mahasiswa})
        
        print("-"*70)
        print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
        print("="*70)
        print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
        print("-"*70)

    else:
        print(f"NIM {nim} tidak ditemukan!!!")
    
    is_done()

def hapus_data():
    print("Silahkan masukkan nama yang akan di hapus,")
    nim = int(input("Nama           : "))
    if nim in data_mahasiswa.keys():
        del data_mahasiswa[nim]
        print(f"Data NIM {nim} berhasil di hapus")

    else:
        print(f"NIM {nim} tidak ditemukan!!!")

    is_done ()

def cari_data():
    print("Silahkan masukkan NIM yang akan di cari,")
    # nim = int(input("NIM           : "))
    # if nim in data_mahasiswa.keys():
    print("-"*70)
    print(f"|{'DAFTAR MAHASISWA':^68}|")
    print("-"*70)
    print(f"|{'Nama':^15}|{'NIM':^10}|{'UTS':^8}|{'UAS':^8}|{'Tugas':^8}|{'Nilai Akhir':^14}|")
    print("="*70)
    print(f"|{'Mohon maaf, fitur ini belum tersedia, mau tanya dosen dulu.':^68}|")
    #     print(f"|{NAMA:^15}|{NIM:^10}|{UTS:^8}|{UAS:^8}|{TUGAS:^8}|{NILAI_AKHIR:^14.2f}|")
    #     print("-"*70)
    # else:
    #     print(f"NIM {nim} tidak ditemukan!!!")

    is_done()

def is_done():
    x = input("Tekan tombol enter untuk melanjutkan!!! ")
    

while True:
    os.system("clear")
    print(f"{'PROGRAM NILAI MAHASISWA':^70}")
    print("="*70)
    print("Silahkan pilih menu :")
    i = input("(T)ambah | (U)bah | (H)apus | (C)ari | (L)ihat | (K)eluar : ")

    #Tambah data
    if i.lower() == 't':
        tambah_data()
    
    #Lihat Data
    elif i.lower() == 'l':
       lihat_data()
       
    #Ubah data
    elif i.lower() == 'u':
        ubah_data()
        no = 1
        

    #Hapus Data
    elif i.lower() == 'h':
        hapus_data()

    #Cari Data
    elif i.lower() == 'c':
        cari_data()
    
    #Keluar
    elif i.lower() == 'k':
        break

    else:
        print("Silahkan pilih menu yang tersedia!!!")
        is_done()
