# Lütfen iznim olmadan herhangi bir platformda paylaşmayın ve ya kullanmayınız. Zaten çok kolay bir proje herkesin yapabileceğini düşünüyorum :). 

print("-" * 40)
print("Hesap Makinesine Hoşgeldiniz.")
print("-" * 40)
print("1 - Toplama İşlemi")
print("2 - Çıkarma İşlemi")
print("3 - Çarpma İşlemi")
print("4 - Bölme İşlemi")
print("-" * 40)

islem = int(input("Yapılacak işlem numarasını giriniz: "))

if islem == 1:
    sayi = int(input("Lütfen 1. Sayıyı Giriniz: "))
    sayi1 = int(input("Lütfen 2. Sayıyı Giriniz: "))
    sonuc = sayi + sayi1

    print("Toplama İşlemi Sonucunuz: ",sonuc)

elif islem == 2:
    sayi = int(input("Lütfen 1. Sayıyı Giriniz: "))
    sayi1 = int(input("Lütfen 2. Sayıyı Giriniz: "))
    sonuc = sayi - sayi1

    print("Çıkarma İşlemi Sonucunuz: ",sonuc)

elif islem == 3:
    sayi = int(input("Lütfen 1. Sayıyı Giriniz: "))
    sayi1 = int(input("Lütfen 2. Sayıyı Giriniz: "))
    sonuc = sayi * sayi1

    print("Çarpma İşlemi Sonucunuz: ",sonuc)

elif islem == 4:
    sayi = int(input("Lütfen 1. Sayıyı Giriniz: "))
    sayi1 = int(input("Lütfen 2. Sayıyı Giriniz: "))
    sonuc = sayi // sayi1 # // kullanmamızın nedeni sonucun ondalıklı değilde tam sayı olarak çıkmasıdır.

    print("Bölme İşlemi Sonucunuz: ",sonuc)

# Lütfen iznim olmadan herhangi bir platformda paylaşmayın ve ya kullanmayınız. Zaten çok kolay bir proje herkesin yapabileceğini düşünüyorum :).
