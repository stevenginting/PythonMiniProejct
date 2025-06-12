tinggi = int(input("Berapa jumlah tinggi piramida yang anda inginkan:"))
#piramida simetris
# for i in range(tinggi):
#     spasi = ' ' * (tinggi-i-1)
#     bintang = '*' * (2*i+1)
#     print(spasi + bintang)
#piramida angka
# for i in range(1,tinggi+1):
#     spasi = ' ' * (tinggi-i)
#     bintang = str(i) * (2*i+1)
#     print(spasi + bintang)
for i in range(tinggi,0,-1):
    spasi = ' ' * (tinggi-i)
    bintang = str(i) * (2*i+1)
    print(spasi + bintang)