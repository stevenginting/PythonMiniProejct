def cek_angka_prima():
    mulai = True
    tanya = int(input("Angka prima berapa yang mau di cek?:"))
    prima =  True
    while mulai == True:
        if tanya < 2:
            print("Angka tidak prima")
        else:
            for i in range(2,int(tanya ** 0.5)+1):
                if tanya % i ==0:
                    prima = False
                    break
        if prima:
            print("Bilangan prima")
        else:
            print("Bilangan bukan prima")
        tanyalagi = input("apakah anda mau cek lagi jika iya ketik 'y' jika tidak 'n'")
        if tanyalagi == 'y':
            cek_angka_prima()
        else :
            mulai = False
cek_angka_prima()