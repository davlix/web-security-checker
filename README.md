# Security Check

Program Security Check adalah sebuah skrip Python yang digunakan untuk memeriksa keamanan situs web. Skrip ini menyediakan beberapa fitur yang berguna untuk memeriksa status code, header keamanan, file robots.txt, potensi injeksi SQL, dan file serta folder sensitif pada suatu situs web.

## Instalasi

1. Pastikan Anda memiliki Python yang terinstal di komputer Anda.
2. Clone repositori ini atau unduh file `websc.py`.
3. Instal library yang diperlukan dengan menjalankan perintah berikut:

pip install requests beautifulsoup4


4. Pastikan Anda juga telah menginstal `sqlmap` dan menambahkannya ke dalam PATH sistem Anda agar dapat digunakan untuk memeriksa injeksi SQL.

## Penggunaan

1. Jalankan skrip `websc.py` dengan menjalankan perintah berikut:

python websc.py


2. Masukkan URL situs web yang ingin Anda periksa.

3. Skrip akan melakukan serangkaian pemeriksaan keamanan pada situs web yang Anda masukkan dan menampilkan hasilnya.

## Fitur

Skrip ini memiliki beberapa fitur berikut:

- Memeriksa kode status situs web untuk memastikan apakah situs tersebut aktif.
- Memeriksa header keamanan seperti HSTS (HTTP Strict Transport Security) dan X-XSS-Protection.
- Memeriksa file robots.txt dan menampilkan isinya.
- Memeriksa potensi injeksi SQL menggunakan library sqlmap.
- Memeriksa keberadaan file dan folder sensitif pada situs web.

Pastikan untuk menggunakan skrip ini dengan bijak dan hanya pada situs web yang Anda memiliki izin untuk memeriksa keamanannya.

## Catatan

- Skrip ini mengandalkan library `requests` untuk melakukan permintaan HTTP ke situs web yang diperiksa.
- Untuk memeriksa injeksi SQL, skrip menggunakan library `sqlmap`. Pastikan Anda telah menginstal dan menambahkannya ke dalam PATH sistem Anda.
- Skrip ini hanya melakukan pemeriksaan keamanan dasar. Untuk keamanan yang lebih komprehensif, disarankan untuk menggunakan alat keamanan yang lebih canggih dan melibatkan profesional keamanan.

## Kontribusi

Anda dapat melakukan kontribusi pada proyek ini dengan mengirimkan permintaan tarik (pull request) untuk perbaikan bug, peningkatan fitur, atau saran lainnya.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk informasi lebih lanjut.




