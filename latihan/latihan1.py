try:
    # Input angka pertama
    angka1 = float(input("Masukkan angka pertama: "))
    # Input angka kedua
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Error: Input harus berupa angka!")
    exit()

# Input operator
operator = input("Masukkan operator (+, -, *, /): ")

try:
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        try:
            hasil = angka1 / angka2
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol!")
            exit()
    else:
        # Operator tidak valid → raise error kustom
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    print("Hasil:", hasil)

except Exception as e:
    print("Error:", e)
