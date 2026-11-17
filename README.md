# DOKNOVA: Aplikasi Kesehatan & Kalkulator TDEE

Aplikasi berbasis terminal (CLI) yang ditulis dengan Python untuk menghitung indikator kesehatan dasar: IMT, BMR, TDEE, dan kebutuhan air harian.

---

## 1. Identitas Kelompok

| Keterangan | Isi |
|---|---|
| **Nama Aplikasi** | DOKNOVA |
| **Nama Kelompok** | _(isi nama kelompok)_ |

### Daftar Anggota & Pembagian Peran

| No | Nama | NPM | Peran |
|---|---|---|---|
| 1 | _(nama anggota 1)_ | _(NPM)_ | _(contoh: Ketua / Pengembang fitur kalkulator)_ |
| 2 | _(nama anggota 2)_ | _(NPM)_ | _(contoh: Pengembang validasi input / utils.py)_ |
| 3 | _(nama anggota 3)_ | _(NPM)_ | _(contoh: Pengembang menu utama / main.py)_ |
| 4 | _(nama anggota 4)_ | _(NPM)_ | _(contoh: Dokumentasi & pengujian)_ |

---

## 2. Deskripsi Aplikasi

DOKNOVA adalah program kalkulator kesehatan yang dijalankan lewat terminal. Pengguna cukup memasukkan data diri seperti jenis kelamin, berat badan, tinggi badan, dan usia, lalu program menghitung hasilnya secara otomatis.

### Masalah yang Diselesaikan

- Banyak orang tidak tahu apakah berat badannya sudah ideal atau belum.
- Menghitung kebutuhan kalori dan air harian secara manual memerlukan rumus yang rumit dan rawan salah hitung.
- Informasi kesehatan dasar biasanya tersebar di banyak situs atau aplikasi yang berbeda.

DOKNOVA menggabungkan empat perhitungan tersebut dalam satu aplikasi sederhana, lengkap dengan validasi input agar data yang dimasukkan tetap masuk akal, serta riwayat perhitungan selama satu sesi.

> **Catatan:** Hasil perhitungan hanya perkiraan umum dan bukan pengganti saran dokter atau ahli gizi.

---

## 3. Daftar Fitur & Cara Penggunaan

Setelah program dijalankan, menu utama akan tampil. Ketik angka menu (1-6) lalu tekan **Enter**.

| Menu | Fitur | Keterangan |
|---|---|---|
| 1 | Hitung IMT / BMI | Menghitung Indeks Massa Tubuh dan menampilkan kategorinya |
| 2 | Hitung BMR | Menghitung kalori dasar yang dibakar tubuh saat istirahat (rumus Mifflin-St Jeor) |
| 3 | Hitung TDEE | Menghitung kebutuhan kalori harian berdasarkan tingkat aktivitas |
| 4 | Asupan Air Harian | Merekomendasikan jumlah air minum per hari |
| 5 | Riwayat Perhitungan | Menampilkan semua hasil perhitungan pada sesi saat ini |
| 6 | Keluar | Menutup program |

### Cara Menggunakan Tiap Fitur

**Menu 1: IMT**
1. Masukkan berat badan (kg) dan tinggi badan (cm).
2. Program menampilkan nilai IMT dan kategorinya:
   - Kurang dari 18,5: Kurus (Underweight)
   - 18,5 sampai kurang dari 25: Normal (Ideal)
   - 25 sampai kurang dari 30: Kelebihan Berat Badan (Overweight)
   - 30 ke atas: Obesitas

**Menu 2: BMR**
1. Masukkan jenis kelamin (`L` / `P`), berat badan, tinggi badan, dan usia.
2. Program menampilkan BMR dalam kkal/hari.

**Menu 3: TDEE**
1. Masukkan data diri seperti pada menu BMR.
2. Pilih tingkat aktivitas harian:
   - 1 = Sedentary (jarang / tidak olahraga)
   - 2 = Ringan (olahraga 1-3 hari/minggu)
   - 3 = Sedang (olahraga 3-5 hari/minggu)
   - 4 = Berat (olahraga 6-7 hari/minggu)
   - 5 = Ekstra berat (pekerja fisik / atlet)
3. Program menampilkan TDEE beserta target kalori untuk menjaga, menurunkan (-500 kkal), dan menaikkan (+500 kkal) berat badan.

**Menu 4: Asupan Air Harian**
1. Masukkan berat badan (kg) dan durasi olahraga hari ini (menit).
2. Program menampilkan rekomendasi air minum dalam liter dan mililiter.
   Rumus: 35 ml x berat badan, ditambah 350 ml untuk setiap 30 menit olahraga.

**Menu 5: Riwayat**
- Menampilkan daftar hasil perhitungan yang sudah dilakukan sejak program dibuka. Riwayat disimpan di memori, sehingga **hilang saat program ditutup**.

### Validasi Input

- Berat badan: 1-500 kg
- Tinggi badan: 30-300 cm
- Usia: 1-120 tahun
- Durasi olahraga: 0-1440 menit
- Jenis kelamin hanya `L` atau `P`
- Input kosong atau bukan angka akan ditolak dan pengguna diminta mengulang.

---

## 4. Penjelasan Alur Logika & Fungsi Tiap File

### Struktur Folder

```
Tugas-Minggu-ke-3/
├── main.py      # Titik masuk program & menu utama
├── fitur.py     # Logika perhitungan & fitur menu
├── utils.py     # Fungsi bantu validasi input
└── README.md    # Dokumentasi
```

### Alur Umum Program

```
main.py (menu utama)
   │  pengguna memilih menu 1-6
   ▼
fitur.py (fitur_menu_...)
   │  meminta input lewat fungsi di utils.py
   │  memanggil fungsi hitung_...
   │  menampilkan hasil & menyimpan ke riwayat
   ▼
kembali ke menu utama (sampai memilih 6 / Keluar)
```

### `main.py`

Berisi tampilan dan alur menu utama.

| Fungsi | Penjelasan |
|---|---|
| `tampilkan_banner()` | Mencetak banner/judul aplikasi |
| `main()` | Perulangan `while True` yang menampilkan menu, membaca pilihan (1-6), lalu memanggil fitur yang sesuai. Berhenti ketika pengguna memilih menu 6 |

Program dimulai dari blok `if __name__ == "__main__": main()`.

### `fitur.py`

Berisi seluruh logika perhitungan dan fitur setiap menu. File ini memiliki variabel global `riwayat_perhitungan` (list of dictionary) untuk menyimpan riwayat sesi.

**Fungsi perhitungan:**

| Fungsi | Penjelasan |
|---|---|
| `hitung_imt(berat_kg, tinggi_cm)` | Menghitung IMT = berat / (tinggi dalam meter)², lalu menentukan kategori. Mengembalikan `(imt, kategori)` |
| `hitung_bmr(gender, berat_kg, tinggi_cm, usia)` | Rumus Mifflin-St Jeor. Pria: `10W + 6.25H - 5A + 5`. Wanita: `10W + 6.25H - 5A - 161` |
| `hitung_tdee(bmr, tingkat_aktivitas)` | BMR dikalikan faktor aktivitas (1.2; 1.375; 1.55; 1.725; 1.9) |
| `hitung_kebutuhan_air(berat_kg, menit_olahraga)` | Air dasar 35 ml/kg ditambah 350 ml per 30 menit olahraga, hasil dalam liter |

**Fungsi input & menu:**

| Fungsi | Penjelasan |
|---|---|
| `input_data_dasar()` | Meminta jenis kelamin, berat, tinggi, dan usia (dipakai bersama oleh menu BMR dan TDEE) |
| `fitur_menu_imt()` | Alur menu IMT: input, hitung, tampilkan, simpan riwayat |
| `fitur_menu_bmr()` | Alur menu BMR |
| `fitur_menu_tdee()` | Alur menu TDEE termasuk pilihan tingkat aktivitas |
| `fitur_menu_air()` | Alur menu asupan air harian |
| `tampilkan_riwayat()` | Mencetak seluruh isi `riwayat_perhitungan` secara berurutan |

### `utils.py`

Berisi fungsi pembantu untuk validasi input. Semuanya menggunakan perulangan `while True` dengan `try-except`, sehingga pengguna terus diminta mengulang sampai input valid.

| Fungsi | Penjelasan |
|---|---|
| `input_angka_bulat(pesan, min_val, max_val)` | Membaca bilangan bulat dalam rentang tertentu |
| `input_angka_float(pesan, min_val, max_val)` | Membaca bilangan desimal dalam rentang tertentu |
| `input_teks_tidak_kosong(pesan)` | Membaca teks dan menolak input kosong |

---

## 5. Cara Menjalankan di Komputer Lain

### Persyaratan

- **Python 3.8 atau lebih baru**
- Tidak membutuhkan library tambahan (hanya memakai modul bawaan Python)

### Langkah-langkah

1. **Pasang Python** dari https://www.python.org/downloads/. Pada Windows, centang **"Add Python to PATH"** saat instalasi.

2. **Cek instalasi** dengan membuka terminal / Command Prompt:
   ```bash
   python --version
   ```
   Pada macOS/Linux, gunakan `python3 --version`.

3. **Salin proyek** ke komputer tersebut. Pilih salah satu cara:
   - Unduh folder proyek (ZIP) lalu ekstrak, atau
   - Gunakan Git:
     ```bash
     git clone <url-repository-anda>
     ```

4. **Masuk ke folder proyek** (pastikan `main.py`, `fitur.py`, dan `utils.py` berada di folder yang sama):
   ```bash
   cd Tugas-Minggu-ke-3
   ```

5. **Jalankan program:**
   ```bash
   python main.py
   ```
   Pada macOS/Linux:
   ```bash
   python3 main.py
   ```

6. Menu utama DOKNOVA akan tampil dan program siap digunakan.

### Pemecahan Masalah

| Masalah | Solusi |
|---|---|
| `'python' is not recognized` | Python belum masuk PATH. Pasang ulang dan centang "Add Python to PATH", atau coba `py main.py` di Windows |
| `ModuleNotFoundError: No module named 'utils'` / `'fitur'` | Jalankan perintah dari dalam folder proyek, dan pastikan ketiga file `.py` berada di folder yang sama |
