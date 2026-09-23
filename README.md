# Studi_kasus_5_Anggitha-Christien-Wulandari

Nama: Anggitha Christien Wulandari

NIM: 2609116036

Program Studi: Sistem Informasi

Deskripsi Program:

Program Sistem Perhitungan Biaya Parkir merupakan program Python yang digunakan untuk menghitung total biaya parkir kendaraan berdasarkan jenis kendaraan dan lama waktu parkir. Program ini menggunakan function untuk melakukan proses perhitungan biaya parkir.

Pengguna diminta memasukkan jenis kendaraan, jam masuk, dan jam keluar. Jenis kendaraan digunakan untuk menentukan tarif parkir, yaitu Rp5.000 per jam untuk mobil dan Rp3.000 per jam untuk motor. Jam masuk dan jam keluar digunakan untuk menghitung lama kendaraan berada di tempat parkir.

Program menggunakan beberapa konsep dasar Python, yaitu function, parameter, percabangan if dan elif, variabel, input(), float(), operasi pengurangan dan perkalian, return, serta print().

Penjelasan Bagian Program:

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


Penjelasan Output Program:

1. Jenis Kendaraan

<img width="400" alt="Screenshot 2026-09-23 115106" src="https://github.com/user-attachments/assets/550daa0d-11d0-4410-8d7f-f3b96c626e17" />

Menunjukkan bahwa kendaraan yang dimasukkan oleh pengguna adalah Mobil. Berdasarkan ketentuan program, mobil memiliki tarif Rp5.000 per jam.

2. Jam Masuk

Jam masuk       : 10.0

Menunjukkan bahwa kendaraan mulai parkir pada jam 10.00.

3. Jam Keluar

Jam keluar      : 16.0

Menunjukkan bahwa kendaraan keluar dari tempat parkir pada jam 16.00.

4. Lama Parkir

Lama parkir     : 6.0 jam

Menunjukkan bahwa kendaraan berada di tempat parkir selama 6 jam, yang diperoleh dari:

16.00 − 10.00 = 6 jam

5. Total Biaya Parkir

Total biaya     : Rp 30000.0

Menunjukkan total biaya yang harus dibayar. Karena kendaraan adalah Mobil dengan tarif Rp5.000 per jam dan lama parkir 6 jam, maka:

Rp5.000 × 6 = Rp30.000

Jadi, total biaya parkir adalah Rp30.000.

<img width="1920" height="1080" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/7b5ae550-c133-4561-9889-1dd6220b398e" />
