import pandas as pd
from sqlalchemy import create_engine
import os

def load_data_to_postgres(csv_path="data/processed/transaksi_clean.csv"):
    if not os.path.exists(csv_path):
        print("❌ File hasil transformasi tidak ditemukan. Jalankan transform_data.py terlebih dahulu.")
        return

    # --- Koneksi ke PostgreSQL ---
    user = "postgres"        # ganti sesuai username PostgreSQL kamu
    password = "Ujb12345"    # ganti sesuai password PostgreSQL kamu
    host = "localhost"
    port = "5432"
    database = "penjualan_db"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    # --- Baca data hasil transformasi ---
    df = pd.read_csv(csv_path)

    # --- Masukkan ke tabel (replace artinya akan ditimpa setiap dijalankan) ---
    table_name = "fakta_penjualan"
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"✅ Data berhasil dimuat ke PostgreSQL tabel '{table_name}' ({len(df)} baris).")

if __name__ == "__main__":
    load_data_to_postgres()
