import random
import string

def generate_complex_number(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(lenght))

try:
    panjang = int(input("Masukan berapa jumlah angka yang ingin di generate:"))
    hasil = generate_complex_number(panjang)
    print("Hasil dari generate number adalah",hasil)
except ValueError:
    print("Ada yang error")