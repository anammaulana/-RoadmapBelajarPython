#  Percabangan (if, else, elif)

# Menggunakan if,  else
print("Menggunakan if,  else")
print("===================================")
inputNilai = int(input("Masukkan nilai: "))
print("variable inputNilai :", inputNilai)
nilai = inputNilai
print("variable nilai :", nilai)

if nilai >= 90:
    print("Nilai A")
else :
    print("Nilai B")
    
# Menggunakan if, elif, else
print("Menggunakan if, elif, else")
print("===================================")
inputNilai = int(input("Masukkan nilai: "))
print("variable inputNilai :", inputNilai)
nilai = inputNilai
print("variable nilai :", nilai)
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")
# Menggunakan if, elif, else dengan operator logika
print("Menggunakan if, elif, else dengan operator logika")
print("===================================")
inputNilai = int(input("Masukkan nilai: "))
print("variable inputNilai :", inputNilai)
nilai = inputNilai
print("variable nilai :", nilai)
if nilai >= 90 and nilai <= 100:
    print("Nilai A")
elif nilai >= 80 and nilai < 90:
    print("Nilai B")
elif nilai >= 70 and nilai < 80:
    print("Nilai C")
elif nilai >= 60 and nilai < 70:
    print("Nilai D")
else:
    print("Nilai E")
# Menggunakan if, elif, else dengan operator logika dan nested if
print("Menggunakan if, elif, else dengan operator logika dan nested if ")
print("===================================")
inputNilai = int(input("Masukkan nilai: "))
print("variable inputNilai :", inputNilai)
nilai = inputNilai
print("variable nilai :", nilai)
if nilai >= 90 and nilai <= 100:
    print("Nilai A")
elif nilai >= 80 and nilai < 90:
    print("Nilai B")
elif nilai >= 70 and nilai < 80:
    print("Nilai C")
elif nilai >= 60 and nilai < 70:
    print("Nilai D")
else:
    print("Nilai E")
    if nilai < 50:
        print("Perlu perbaikan")
    else:
        print("Perlu perhatian lebih")
