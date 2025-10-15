import pandas as pd
import os

def transform_data(input_path="data/raw/transaksi.csv", output_path="data/processed/transaksi_clean.csv"):
    # Pastikan file input ada
    if not os.path.exists(input_path):
        print("❌ File input tidak ditemukan. Jalankan extract_data.py terlebih dahulu.")
        return
    
    # Pastikan folder output ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Baca data mentah
    df = pd.read_csv(input_path)

    print("📥 Membaca data mentah...")
    print(f"Jumlah baris sebelum dibersihkan: {len(df)}")

    # 1️⃣ Hapus duplikat
    df = df.drop_duplicates()

    # 2️⃣ Hapus data yang kolom pentingnya kosong
    df = df.dropna(subset=["tanggal_transaksi", "jumlah", "harga_satuan"])

    # 3️⃣ Ubah format tanggal ke datetime
    df["tanggal_transaksi"] = pd.to_datetime(df["tanggal_transaksi"], errors="coerce")

    # 4️⃣ Tambahkan kolom total_harga
    df["total_harga"] = df["jumlah"] * df["harga_satuan"]

    # 5️⃣ Tangani data tanggal kosong atau salah format
    df = df.dropna(subset=["tanggal_transaksi"])

    # 6️⃣ Urutkan data berdasarkan tanggal
    df = df.sort_values(by="tanggal_transaksi")

    # Simpan hasil transformasi
    df.to_csv(output_path, index=False)
    print(f"✅ Data berhasil dibersihkan dan disimpan ke {output_path}")
    print(f"Jumlah baris setelah dibersihkan: {len(df)}")

    return df

if __name__ == "__main__":
    transform_data()
