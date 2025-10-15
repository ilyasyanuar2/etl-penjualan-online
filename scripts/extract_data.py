import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_dummy_data(output_path="data/raw/transaksi.csv" , jumlah_data=500):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    produk = [
        {"id": 1, "nama": "Headphone Bluetooth", "kategori": "Elektronik", "harga": 250000},
        {"id": 2, "nama": "Kaos Polos Unisex", "kategori": "Fashion", "harga": 70000},
        {"id": 3, "nama": "Mouse Wireless", "kategori": "Elektronik", "harga": 120000},
        {"id": 4, "nama": "Botol Minum 1L", "kategori": "Perlengkapan Rumah", "harga": 45000},
        {"id": 5, "nama": "Tas Selempang Canvas", "kategori": "Fashion", "harga": 180000},
    ]

    metode = ["Transfer Bank", "COD", "E-Wallet", "Kartu Kredit"]
    kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan"]

    data = []
    start_date = datetime(2024, 1, 1)

    for i in range(1, jumlah_data + 1):
        p = random.choice(produk)
        tgl = start_date + timedelta(days=random.randint(0, 270))
        jumlah = random.randint(1, 5)
        metode_bayar = random.choice(metode)
        city = random.choice(kota)

        data.append({
            "id_transaksi": i,
            "tanggal_transaksi": tgl.strftime("%Y-%m-%d"),
            "id_produk": p["id"],
            "nama_produk": p["nama"],
            "kategori": p["kategori"],
            "jumlah": jumlah,
            "harga_satuan": p["harga"],
            "metode_pembayaran": metode_bayar,
            "kota_pelanggan": city
        })
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"✅ File transaksi.csv berhasil dibuat di {output_path} ({len(df)} baris).")

if __name__ == "__main__":
    generate_dummy_data()