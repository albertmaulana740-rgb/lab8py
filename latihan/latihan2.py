nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        total += float(n)   # mencoba mengubah ke angka
        jumlah_data += 1
    except ValueError:
        # Jika data bukan angka, lewati
        print(f"Data '{n}' dilewati (bukan angka).")
        continue

if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print(f"\nRata-rata nilai valid: {rata_rata}")
else:
    print("Tidak ada data angka yang valid.")
