
def en_uzun_ardisik_dizi(nums):
    sayilar = set(nums)  # hızlı arama için
    en_uzun = 0

    for sayi in sayilar:
        if (sayi - 1) not in sayilar:  # sadece ardışık serinin başlangıcında başla
            mevcut = sayi
            uzunluk = 1

            while (mevcut + 1) in sayilar:
                mevcut += 1
                uzunluk += 1

            en_uzun = max(en_uzun, uzunluk)

    return en_uzun


# Test
num = [1, 2, 3, 400, 76, 45, 32, 56, 64, 78, 68, 899]
print(en_uzun_ardisik_dizi(num))  # Çıktı: 3 → çünkü 1,2,3 ardışık
