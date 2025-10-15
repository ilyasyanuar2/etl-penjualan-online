🧩 ETL Pipeline dan Data Warehouse untuk Analisis Penjualan Toko Online
📘 Deskripsi Proyek

Proyek ini merupakan implementasi sederhana dari ETL Pipeline (Extract, Transform, Load) menggunakan Python dan PostgreSQL.
Tujuannya adalah untuk mengelola data transaksi penjualan toko online, mulai dari proses ekstraksi, pembersihan, hingga pemuatan data ke dalam Data Warehouse (PostgreSQL) agar bisa dianalisis oleh tim Business Intelligence.

🧱 Arsitektur Proyek
[Extract]   → Mengambil data transaksi dari file CSV
[Transform] → Membersihkan data dan menambahkan kolom total_harga
[Load]      → Menyimpan hasil transformasi ke PostgreSQL Data Warehouse
[Analyze]   → Mengambil data dari PostgreSQL untuk analisis dan visualisasi

⚙️ Teknologi yang Digunakan
Komponen	Deskripsi
Python (Pandas, SQLAlchemy, Matplotlib)	Untuk proses ETL dan visualisasi data
PostgreSQL	Sebagai Data Warehouse
pgAdmin / Metabase	Untuk query SQL dan pembuatan dashboard
Jupyter Notebook (opsional)	Untuk eksplorasi data dan analisis tambahan
📂 Struktur Folder
etl_penjualan/
│
├── data/
│   ├── raw/
│   │   └── transaksi_raw.csv           # Data mentah (hasil generate)
│   └── processed/
│       └── transaksi_clean.csv         # Data hasil transformasi
│
├── scripts/
│   ├── extract_data.py                 # Membuat/mengambil data transaksi
│   ├── transform_data.py               # Membersihkan data
│   ├── load_data.py                    # Memuat data ke PostgreSQL
│   └── analyze_data.py                 # Analisis dan visualisasi
│
├── requirements.txt                    # Library yang dibutuhkan
└── README.md                           # Dokumentasi proyek

🚀 Langkah Menjalankan Proyek
1️⃣ Clone repository
git clone https://github.com/username/etl-penjualan-online.git
cd etl-penjualan-online

2️⃣ Install library Python
pip install -r requirements.txt

3️⃣ Jalankan proses ETL
# Generate data transaksi
python scripts/extract_data.py

# Bersihkan dan transformasi data
python scripts/transform_data.py

# Muat ke PostgreSQL
python scripts/load_data.py


Pastikan PostgreSQL sudah terinstal dan database penjualan_db sudah dibuat.
Ganti username/password di file load_data.py sesuai dengan konfigurasi lokal kamu.

4️⃣ Jalankan Analisis & Visualisasi
python scripts/analyze_data.py

📊 Contoh Hasil Analisis
🔹 Total Penjualan per Bulan

Grafik garis menunjukkan tren penjualan tiap bulan.

🔹 Top 5 Produk Terlaris

Menampilkan produk dengan jumlah penjualan tertinggi.

🔹 Kota dengan Penjualan Terbesar

Membantu mengetahui area paling potensial.

🔹 Metode Pembayaran Terpopuler

Distribusi transaksi berdasarkan metode pembayaran.

💡 Insight yang Dihasilkan

Terlihat bahwa kategori Elektronik mendominasi penjualan bulanan.

Metode pembayaran Transfer Bank paling banyak digunakan.

Kota Jakarta dan Surabaya memberikan kontribusi terbesar terhadap total penjualan.

🧠 Pelajaran yang Didapat

Dari proyek ini saya belajar bagaimana:

Merancang alur kerja ETL end-to-end

Menggunakan Python + Pandas untuk transformasi data

Mengelola dan memuat data ke PostgreSQL Data Warehouse

Membuat visualisasi analitik sederhana untuk mendukung pengambilan keputusan

✨ Pengembangan Selanjutnya

Menjadwalkan pipeline ETL otomatis dengan Apache Airflow

Menambahkan dashboard interaktif menggunakan Metabase / Power BI

Mengintegrasikan API eksternal untuk mendapatkan data penjualan real-time

👨‍💻 Tentang Pembuat

Proyek ini dibuat sebagai bagian dari portofolio Data Engineer untuk menunjukkan pemahaman terhadap konsep ETL dan Data Warehouse.

📧 Email: [your.email@gmail.com
]
🔗 LinkedIn: [linkedin.com/in/yourprofile]
💻 GitHub: [github.com/yourusername]

✅ Lisensi

Proyek ini bersifat open-source dan dapat digunakan untuk keperluan pembelajaran.