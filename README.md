# TeksisterAPI
Deskripsi : Berisi source code python untuk tugas mata kuliah teksister dalam pembuatan API 
yang bertugas untuk mengembalikan informasi dalam bentuk json dari hasil crawling web e-commerce BukaLapak

Penjelasan File :
1. Account : File berisi controller dan file handler untuk metode PUT PUSH DELETE GET account 
2. Crawler : File berisi pendefinisian get crawling data BukaLapak dan crawling pagination BukaLapak
3. Html : Karena website BukaLapak sering berubah strukturnya maka untuk mengantisipasi perubahan struktur
   setiap crawling akan mensave terlebih dahulu bukalapak menjadi sebuah HTML
4. Server : Untuk menghandle parsing endpoint tanpa Flask
5. Main : main dari program API ini

Penggunaan :
1. Terdapat beberapa endpoint yang bisa diakses melalui web browser
  - http://localhost:3000/ -> halaman utama
  - http://localost:3000/tas -> menghasilkan Json harga, kategori dan nama tas BukaLapak
  - http://localost:3000/sandal -> menghasilkan Json harga, kategori dan nama sandal BukaLapak
  - http://localost:3000/jumpsuit -> menghasilkan Json harga, kategori dan jumpsuit tas BukaLapak
  - http://localost:3000/kaos -> menghasilkan Json harga, kategori dan nama kaos BukaLapak
  - http://localost:3000/poloshirt -> menghasilkan Json harga, kategori dan nama poloshirt BukaLapak
 2. Menggunakan postman
   - Dapat menggunakan metode PUSH account (nama,email,username) 
   - Dapat menggunakan metode PUT untuk mengupdate account
   - Dapat menggunakan metode DELETE untuk menghapus account
   - Dapat menggunakan metode GET untuk mendapat semua info akun yang ada
   - Dapat menggunakan metode GET seperti di web browser
 
<<<<<<< HEAD
 Thank You :D
=======
 Thank You :D
>>>>>>> 032ce1581db940e2db258622e6814c39e2babbca
