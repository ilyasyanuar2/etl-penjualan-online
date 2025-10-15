import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# --- Koneksi ke PostgreSQL ---
user = "postgres"        # ganti sesuai username PostgreSQL kamu
password = "Ujb12345"    # ganti sesuai password PostgreSQL kamu
host = "localhost"
port = "5432"
database = "penjualan_db"

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# --- Ambil data dari tabel fakta_penjualan ---
query = "SELECT * FROM fakta_penjualan"
df = pd.read_sql(query, engine)

print("✅ Data berhasil diambil dari PostgreSQL.")
print(df.head())

# --- Analisis 1: Total Penjualan per Bulan ---
df['tanggal_transaksi'] = pd.to_datetime(df['tanggal_transaksi'])
df['bulan'] = df['tanggal_transaksi'].dt.to_period('M')
penjualan_bulanan = df.groupby('bulan')['total_harga'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(penjualan_bulanan['bulan'].astype(str), penjualan_bulanan['total_harga'], marker='o')
plt.title("Total Penjualan per Bulan")
plt.xlabel("Bulan")
plt.ylabel("Total Penjualan (Rp)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Analisis 2: Produk Terlaris ---
produk_terlaris = df.groupby('nama_produk')['jumlah'].sum().sort_values(ascending=False).head(5)

produk_terlaris.plot(kind='bar', figsize=(8,4), title='Top 5 Produk Terlaris')
plt.ylabel("Jumlah Terjual")
plt.tight_layout()
plt.show()

# --- Analisis 3: Kota dengan Penjualan Tertinggi ---
kota_tertinggi = df.groupby('kota_pelanggan')['total_harga'].sum().sort_values(ascending=False).head(5)

kota_tertinggi.plot(kind='bar', figsize=(8,4), title='Top 5 Kota dengan Penjualan Tertinggi')
plt.ylabel("Total Penjualan (Rp)")
plt.tight_layout()
plt.show()

# --- Analisis 4: Distribusi Metode Pembayaran ---
metode_pembayaran = df['metode_pembayaran'].value_counts()

metode_pembayaran.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6), title='Metode Pembayaran yang Digunakan')
plt.ylabel("")
plt.show()