import sqlite3

def setup_database():
    """Membuat database dan tabel jika belum ada"""
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS users')
    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            keahlian TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database dan tabel telah diatur.")

def tambah_pengguna(nama, usia, keahlian, jurusan):
    """Menambahkan pengguna baru ke database"""
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (name, age, keahlian, jurusan) VALUES (?, ?, ?, ?)', (nama, usia, keahlian, jurusan))
        conn.commit()
        print(f"Pengguna {nama} berhasil ditambahkan.")
    except sqlite3.Error as e:
        print(f"Terjadi kesalahan: {e}")
    conn.close()

def tampilkan_pengguna():
    """Menampilkan semua pengguna dari database dalam format tabel"""
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT id, name, age, keahlian, jurusan FROM users')
    pengguna = c.fetchall()
    conn.close()
    
    if pengguna:
        print("\nDaftar Pengguna:")
        print(f"{'ID':<5} {'Nama':<20} {'Usia':<5} {'Keahlian':<20} {'Jurusan':<20}")
        print("-" * 70)  # Garis pemisah atas
        for user in pengguna:
            print(f"{user[0]:<5} {user[1]:<20} {user[2]:<5} {user[3]:<20} {user[4]:<20}")
    else:
        print("Tidak ada pengguna ditemukan.")

def hapus_pengguna(user_id):
    """Menghapus pengguna berdasarkan ID"""
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        print(f"Pengguna dengan ID {user_id} telah dihapus.")
    except sqlite3.Error as e:
        print(f"Terjadi kesalahan: {e}")
    conn.close()

def main():
    setup_database()
    
    print("Selamat datang!")
    
    while True:
        print("\n1. Tambah Pengguna")
        print("2. Tampilkan Pengguna")
        print("3. Hapus Pengguna")
        print("4. Keluar")
        pilihan = input("\nPilih opsi (1, 2, 3 atau 4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama Anda: ")
            usia = input("Masukkan usia Anda: ")
            keahlian = input("Masukkan Keahlian Anda: ")
            jurusan = input("Masukkan Jurusan Yang Anda Inginkan: ")
            
            try:
                if not nama.strip() or not keahlian.strip() or not jurusan.strip():
                    raise ValueError("Data tidak boleh dikosongkan, harap diisi.")
                
                usia = int(usia)
                tambah_pengguna(nama, usia, keahlian, jurusan)
            
            except ValueError as e:
                print(e)
        
        elif pilihan == '2':
            tampilkan_pengguna()
        
        elif pilihan == '3':
            try:
                user_id = input("Masukkan ID pengguna yang akan dihapus: ")
                
                if not user_id.strip():
                    raise ValueError("ID pengguna tidak boleh kosong.")
                
                hapus_pengguna(int(user_id))
            
            except ValueError as e:
                print(e)
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        
        else:
            print("Opsi tidak valid. Harap pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
