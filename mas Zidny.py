import random
angka = random.randrange(0,11)
tebak = 0

while tebak < 3 :
    tebak += 1
    tebakan = int(input('masukkan angka tebakanmu! : '))
    if angka > tebakan :
        print('terlalu kecil')
    elif angka < tebakan :
        print('terlalu besar')
    elif angka == tebakan :
        print('selamat tebakan anda benar!!')
        break       
else :
    print('game over')

print('tebakan yang benar adalah :', angka)
