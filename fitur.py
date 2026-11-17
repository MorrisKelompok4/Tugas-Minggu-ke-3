from utils import input_angka_bulat, input_angka_float, input_teks_tidak_kosong

# Data disimpan di dalam list secara dinamis selama program berjalan
riwayat_perhitungan = []

def hitung_imt(berat_kg, tinggi_cm):
  tinggi_m = tinggi_cm / 100
  imt = berat_kg / (tinggi_m**2)

  if imt < 18.5:
    kategori = "Kurus (Underweight)"
  elif 18.5 <= imt < 25.0:
    kategori = "Normal (Ideal)"
  elif 25.0 <= imt < 30.0:
    kategori = "Kelebihan Berat Badan (Overweight)"
  else:
    kategori = "Obesitas"

  return imt, kategori

def hitung_bmr(gender, berat_kg, tinggi_cm, usia):
  # Formula Mifflin-St Jeor (diperbaiki operator perkaliannya)
  if gender.lower() in ["l", "laki-laki", "pria"]:
    bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * usia) + 5
  else:
    bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * usia) - 161
  return bmr

def hitung_tdee(bmr, tingkat_aktivitas):
  faktor_aktivitas = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
  multiplier = faktor_aktivitas.get(tingkat_aktivitas, 1.2)
  tdee = bmr * multiplier
  return tdee

def hitung_kebutuhan_air(berat_kg, menit_olahraga=0):
  air_dasar_ml = berat_kg * 35
  air_tambahan_ml = (menit_olahraga / 30) * 350
  total_ml = air_dasar_ml + air_tambahan_ml
  return total_ml / 1000

def input_data_dasar():
  print("\n--- INPUT DATA DIRI ---")
  gender = input_teks_tidak_kosong("Jenis Kelamin (L/P): ").upper()
  while gender not in ["L", "P"]:
    print("Error: Masukkan L atau P.")
    gender = input_teks_tidak_kosong("Jenis Kelamin (L/P): ").upper()

  berat = input_angka_float("Berat badan (kg): ", min_val=1.0, max_val=500.0)
  tinggi = input_angka_float("Tinggi badan (cm): ", min_val=30.0, max_val=300.0)
  usia = input_angka_bulat("Usia (tahun): ", min_val=1, max_val=120)

  return gender, berat, tinggi, usia

def fitur_menu_imt():
  print("\n--- KALKULATOR IMT ---")
  berat = input_angka_float("Berat badan (kg): ", min_val=1.0, max_val=500.0)
  tinggi = input_angka_float("Tinggi badan (cm): ", min_val=30.0, max_val=300.0)
  imt, kategori = hitung_imt(berat, tinggi)
  print(f"\n[Hasil] IMT Anda: {imt:.2f}")
  print(f"[Kategori]: {kategori}")

  # Menyimpan hasil perhitungan ke dalam riwayat
  riwayat_perhitungan.append(
      {"jenis": "IMT", "detail": f"IMT: {imt:.2f} ({kategori})"}
  )

def fitur_menu_bmr():
  print("\n--- KALKULATOR BMR ---")
  gender, berat, tinggi, usia = input_data_dasar()
  bmr = hitung_bmr(gender, berat, tinggi, usia)
  print(f"\n[Hasil] BMR Anda: {bmr:.2f} kcal/hari")
  print("(Jumlah kalori dasar yang dibakar tubuh saat istirahat total)")

  riwayat_perhitungan.append({"jenis": "BMR", "detail": f"BMR: {bmr:.2f} kcal"})

def fitur_menu_tdee():
  print("\n--- KALKULATOR TDEE (KEBUTUHAN KALORI HARIAN) ---")
  gender, berat, tinggi, usia = input_data_dasar()
  bmr = hitung_bmr(gender, berat, tinggi, usia)

  print("\nTingkat Aktivitas Harian:")
  print("1. Sedentary (Jarang / Tidak Olahraga)")
  print("2. Ringan (Olahraga 1-3 hari/minggu)")
  print("3. Sedang (Olahraga 3-5 hari/minggu)")
  print("4. Berat (Olahraga 6-7 hari/minggu)")
  print("5. Ekstra Berat (Pekerja Fisik / Atlet)")

  akt = input_angka_bulat("Pilih tingkat aktivitas (1-5): ", min_val=1, max_val=5)
  tdee = hitung_tdee(bmr, akt)

  print(f"\n[Hasil TDEE]: {tdee:.2f} kcal/hari")
  print(f"- Untuk menjaga berat badan : {tdee:.0f} kcal")
  print(f"- Untuk menurunkan berat badan (-500 kcal): {tdee - 500:.0f} kcal")
  print(f"- Untuk menaikkan berat badan (+500 kcal) : {tdee + 500:.0f} kcal")

  riwayat_perhitungan.append({"jenis": "TDEE", "detail": f"TDEE: {tdee:.2f} kcal"})

def fitur_menu_air():
  print("\n--- KALKULATOR ASUPAN AIR HARIAN ---")
  berat = input_angka_float("Berat badan (kg): ", min_val=1.0, max_val=500.0)
  olahraga = input_angka_float(
      "Durasi olahraga hari ini (menit): ", min_val=0.0, max_val=1440.0
  )
  air_liter = hitung_kebutuhan_air(berat, olahraga)
  print(
      f"\n[Hasil] Rekomendasi air minum harian: {air_liter:.2f} Liter"
      f" ({air_liter * 1000:.0f} ml)"
  )

  riwayat_perhitungan.append(
      {"jenis": "Asupan Air", "detail": f"Rekomendasi Air: {air_liter:.2f} Liter"}
  )

def tampilkan_riwayat():
  print("\n--- RIWAYAT PERHITUNGAN SESI INI ---")
  if not riwayat_perhitungan:
    print("Belum ada riwayat perhitungan yang tercatat.")
  else:
    for i, item in enumerate(riwayat_perhitungan, 1):
      print(f"{i}. [{item['jenis']}] {item['detail']}")