def input_angka_bulat(pesan, min_val=None, max_val=None):
  """Memastikan input berupa angka bulat dan dalam rentang wajar."""
  while True:
    try:
      val = int(input(pesan))
      if min_val is not None and val < min_val:
        print(f"Error: Angka minimal adalah {min_val}.")
        continue
      if max_val is not None and val > max_val:
        print(f"Error: Angka maksimal adalah {max_val}.")
        continue
      return val
    except ValueError:
      print("Error: Masukkan angka bulat yang valid!")

def input_angka_float(pesan, min_val=None, max_val=None):
  """Memastikan input berupa angka desimal dan dalam rentang wajar."""
  while True:
    try:
      val = float(input(pesan))
      if min_val is not None and val < min_val:
        print(f"Error: Angka minimal adalah {min_val}.")
        continue
      if max_val is not None and val > max_val:
        print(f"Error: Angka maksimal adalah {max_val}.")
        continue
      return val
    except ValueError:
      print("Error: Masukkan angka yang valid!")

def input_teks_tidak_kosong(pesan):
  """Memastikan input teks tidak kosong."""
  while True:
    teks = input(pesan).strip()
    if teks:
      return teks
    print("Error: Input tidak boleh kosong.")