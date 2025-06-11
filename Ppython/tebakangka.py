import random

angka_rahasia = random.randint(1, 60)

print("=== Game Tebak Angka ===")
print("Tebak angka antara 1 hingga 1000!")

tebakan = None
percobaan = 0
maksimal = 5

while tebakan != angka_rahasia and percobaan < maksimal:
    try:
        tebakan = int(input(f"Tebakan ke-{percobaan + 1}: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil!\n")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!\n")
        else:
            print(f"🎉 Selamat! Kamu benar. Angkanya adalah {angka_rahasia}.")
            print(f"Kamu menebak dengan benar dalam {percobaan} percobaan.")
            break

    except ValueError:
        print("Masukkan angka yang valid!\n")

# Jika gagal dalam 5 kali
if tebakan != angka_rahasia:
    print(f"😢 Game Over! Kamu kehabisan percobaan. Angka yang benar adalah {angka_rahasia}.")