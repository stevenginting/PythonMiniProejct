def perkalian(a,b):
    return a * b
def pembagian(a,b):
    return a / b
def pengurangan(a,b):
    return a - b
def penjumlahan(a,b):
    return a + b

operator = {
    "+" : penjumlahan,
    "-" : pengurangan,
    "*" : perkalian,
    "/" : pembagian,
}
def kalkulator():
    mulai = True
    num1 = float(input("Ketik lah angka pertama:"))
    while mulai == True:
        for i in operator:
            print(i,end="")
        simbol_operasi = input("Pilih operasi yang ingin kamu pakai:")
        num2 = float(input("Ketik lah angka kedua:"))
        jawaban  = operator[simbol_operasi](num1,num2)
        print(jawaban)

        pilih = input("Kalau kami ingin lanjut ketik 'y' jika tidak 'n'")
        if pilih == 'y':
            kalkulator()
kalkulator()