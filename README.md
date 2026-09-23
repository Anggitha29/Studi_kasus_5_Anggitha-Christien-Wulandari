# Studi_kasus_5_Anggitha-Christien-Wulandari

Nama: Anggitha Christien Wulandari

NIM: 2609116036

Program Studi: Sistem Informasi





**Deskripsi Program:**

Program Sistem Perhitungan Biaya Parkir merupakan program Python yang digunakan untuk menghitung total biaya parkir kendaraan berdasarkan jenis kendaraan dan lama waktu parkir. Program ini menggunakan function untuk melakukan proses perhitungan biaya parkir.

Pengguna diminta memasukkan jenis kendaraan, jam masuk, dan jam keluar. Jenis kendaraan digunakan untuk menentukan tarif parkir, yaitu Rp5.000 per jam untuk mobil dan Rp3.000 per jam untuk motor. Jam masuk dan jam keluar digunakan untuk menghitung lama kendaraan berada di tempat parkir.

Program menggunakan beberapa konsep dasar Python, yaitu function, parameter, percabangan if dan elif, variabel, input(), float(), operasi pengurangan dan perkalian, return, serta print().





**Penjelasan Struktur Program:**

1. Function
Function hitung_biaya_parkir() digunakan untuk melakukan proses perhitungan total biaya parkir berdasarkan jenis kendaraan dan lama parkir.

2. Parameter
Function memiliki parameter jenis_kendaraan dan durasi. jenis_kendaraan digunakan untuk menentukan tarif, sedangkan durasi digunakan untuk menentukan lama parkir.

3. Percabangan if dan elif
Digunakan untuk menentukan tarif berdasarkan jenis kendaraan. Mobil memiliki tarif Rp5.000 per jam, sedangkan motor Rp3.000 per jam.

4. input()
Digunakan untuk menerima data dari pengguna berupa jenis kendaraan, jam masuk, dan jam keluar.

5. float()
Digunakan agar input jam dapat berupa angka desimal, misalnya 10.00 dan 16.00.

6. Perhitungan lama parkir
Lama parkir dihitung dengan mengurangi jam keluar dengan jam masuk.

7. Perhitungan biaya
Total biaya dihitung dengan mengalikan tarif parkir dengan lama parkir.

8. return
Digunakan untuk mengembalikan hasil total biaya dari function.

9. print()
Digunakan untuk menampilkan hasil akhir berupa jenis kendaraan, jam masuk, jam keluar, lama parkir, dan total biaya parkir.





**Penjelasan Output Program:**

1. Jenis Kendaraan

<img width=500 alt="Screenshot 2026-09-23 115106" src="https://github.com/user-attachments/assets/526e1970-7a6e-4e2c-a547-a40b2e403ba2" />

Pada bagian ini, program menampilkan jenis kendaraan yang dipilih oleh pengguna, yaitu Mobil. Jenis kendaraan ini digunakan oleh program untuk menentukan tarif parkir yang sesuai. Berdasarkan ketentuan program, tarif parkir untuk Mobil adalah Rp5.000 per jam. Jadi, setelah pengguna memilih Mobil, program akan menggunakan tarif tersebut dalam proses perhitungan biaya parkir.

2. Jam Masuk

<img width=300 alt="Screenshot 2026-09-23 115235" src="https://github.com/user-attachments/assets/432dbe76-a376-4423-8b4f-ca91e83b3638" />

Bagian ini menunjukkan waktu kendaraan mulai masuk dan parkir, yaitu pukul 10.00. Data jam masuk digunakan sebagai salah satu nilai untuk menghitung berapa lama kendaraan berada di tempat parkir. Karena input menggunakan tipe data float, waktu 10.00 ditampilkan oleh Python sebagai 10.0, tetapi nilainya tetap menunjukkan pukul 10.00.

3. Jam Keluar

<img width=300 alt="Screenshot 2026-09-23 115301" src="https://github.com/user-attachments/assets/7a93fd80-7f52-448b-af4d-e339e0497101" />

Bagian ini menunjukkan waktu kendaraan keluar dari tempat parkir, yaitu pukul 15.00. Jam keluar digunakan bersama dengan jam masuk untuk menentukan lama kendaraan parkir. Sama seperti jam masuk, angka 15.0 merupakan hasil tampilan dari tipe data float dan tetap menunjukkan pukul 15.00.

4. Lama Parkir

<img width=300 alt="Screenshot 2026-09-23 145328" src="https://github.com/user-attachments/assets/e5e28425-0cb9-4e79-b8a0-dd6d506872d1" />

Bagian ini menunjukkan total waktu kendaraan berada di tempat parkir, yaitu selama 5 jam. Lama parkir diperoleh dengan mengurangi jam keluar dengan jam masuk:

15.00 − 10.00 = 5 jam

Hasil tersebut kemudian digunakan dalam perhitungan total biaya parkir. Tampilan 5.0 jam muncul karena nilai durasi disimpan dalam tipe data float.

5. Total Biaya Parkir

<img width=300 alt="Screenshot 2026-09-23 145439" src="https://github.com/user-attachments/assets/93deb82d-ffc9-4a04-94b8-184792edbe29" />

Bagian ini merupakan hasil akhir perhitungan biaya parkir. Karena kendaraan yang digunakan adalah Mobil dengan tarif Rp5.000 per jam dan lama parkir adalah 5 jam, maka biaya parkir dihitung dengan mengalikan tarif dengan durasi parkir:

Rp5.000 × 5 jam = Rp25.000

Dengan demikian, total biaya yang harus dibayar untuk kendaraan tersebut adalah Rp25.000. Nilai ditampilkan sebagai Rp 25000.0 karena hasil perhitungan menggunakan tipe data float.


**Bukti Hasil Output Program**

<img width="683" height="170" alt="Screenshot 2026-09-23 151313" src="https://github.com/user-attachments/assets/3a9588d4-1fc8-40e2-ba9b-8231196a154c" />

