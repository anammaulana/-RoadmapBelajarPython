# Buat program untuk menentukan apakah tahun kabisat atau bukan.
print("=== Cek Tahun Kabisat ===")
print("Program ini akan menentukan apakah tahun yang Anda masukkan adalah tahun kabisat atau bukan.")
tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
    
# Contoh: cek apakah angka ganjil atau genap.
print("=== Cek Angka Ganjil atau Genap ===")
print("Program ini akan menentukan apakah angka yang Anda masukkan adalah ganjil atau genap.")
angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")