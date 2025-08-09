#kullanıcı int girer
#girdiği sayı kadar tek sayıları hesaplar (kullancı tek sayı girmelidir)
#sonucu ekrana iletir

#yöntem 1
def tek_sayi_hesapla():

	n = int(input("lütfen bir sayı giriniz = "))

	for i in range(n):
		if n%2==1:
			n += n
			print(f"{n}")

tek_sayi_hesapla()

#yöntem 2
def teksayihesapla():
	n = int(input("lütfen bir sayı giriniz = "))

	toplam = 0

	for i in range(n):
		if i%2==0:
			toplam += i
			print(f"{i}")

teksayihesapla()

#algoritma baslat
#def baslat():
#	tek_sayi_hesapla()
#	teksayihesapla()

#baslat()