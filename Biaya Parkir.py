def hitung_biaya_parkir(jenis_kendaraan, durasi):
    if jenis_kendaraan == "Mobil" :
        tarif = 5000
    elif jenis_kendaraan == "Motor" :
        tarif = 3000

    total = tarif * durasi
    return total 

jenis = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = float(input("Masukkan jam masuk: "))
jam_keluar = float(input("Masukkan jam keluar: "))

lama_parkir = jam_keluar - jam_masuk

biaya = hitung_biaya_parkir(jenis, lama_parkir)

print("TOTAL BIAYA PARKIR")
print("Jenis kendaraan :", jenis)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir, "jam")
print("Total biaya     : Rp", biaya)