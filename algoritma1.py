from collections import Counter

def encok(kelimeler):
    tekrar_sayisi = Counter(kelimeler)
    eleman, kelime = tekrar_sayisi.most_common(1)[0]
    return eleman, kelime

    giris_dizi = ["banana","selamla","banana","hola"]
    eleman, tekrar_sayisi = encok(giris_dizi)
    print(eleman, tekrar_sayisi)

encok()
