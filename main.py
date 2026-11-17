from fitur import (
    fitur_menu_air,
    fitur_menu_bmr,
    fitur_menu_imt,
    fitur_menu_tdee,
    tampilkan_riwayat,
)
from utils import input_angka_bulat

BANNER = r"""
   ____   ___  _  ___   _  _____     ___
   |  _ \ / _ \| |/ / \ | |/ _ \ \   / / \
   | | | | | | | ' /|  \| | | | \ \ / / _ \
   | |_| | |_| | . \| |\  | |_| |\ V / ___ \
   |____/ \___/|_|\_\_| \_|\___/  \_/_/   \_\
   """

def tampilkan_banner():
  print("\n" + "=" * 48)
  print(BANNER)
  print("    + Aplikasi Kesehatan & Kalkulator TDEE +")
  print("=" * 48)

def main():
  while True:
    tampilkan_banner()
    print("1. Hitung Indeks Massa Tubuh (IMT / BMI)")
    print("2. Hitung BMR (Mifflin-St Jeor)")
    print("3. Hitung Kebutuhan Kalori Harian (TDEE)")
    print("4. Hitung Rekomendasi Asupan Air Harian")
    print("5. Lihat Riwayat Perhitungan Sesi")
    print("6. Keluar")

    pilihan = input_angka_bulat("Pilih menu (1-6): ", min_val=1, max_val=6)

    if pilihan == 1:
      fitur_menu_imt()
    elif pilihan == 2:
      fitur_menu_bmr()
    elif pilihan == 3:
      fitur_menu_tdee()
    elif pilihan == 4:
      fitur_menu_air()
    elif pilihan == 5:
      tampilkan_riwayat()
    elif pilihan == 6:
      print(
          "\nTerima kasih telah menggunakan DOKNOVA. Tetap jaga"
          " kesehatan!"
      )
      break

if __name__ == "__main__":
  main()