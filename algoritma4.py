#kullanıcı giriş ve bitiş int değer alınır
# if-else yapısı ile de kontrol edilir
# eğer giriş sonucu bitiş'den büyük ise hata versin
#girilen değerler asal mı diye kontrol edilsin

def algoritma4():
    #kullanıcıdan iste
    sor1 = int(input("lütfen 1.sayıyı girin"))
    sor2 = int(input("lütfen 2.sayıyı girin"))

    if sor1 >= sor2 and sor2 >= sor1:
        print("hata girişi ve bitiş sayıları eşit veya küçük olamaz")
    else:
        if sor1%2 == 1:
            print("giriş sayısı asaldır")
        else:

algoritma()
