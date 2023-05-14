#test version Ix0
import random

turkce_kelimeler = ['araba', 'bilgisayar', 'elma', 'kedi', 'telefon']
ingilizce_kelimeler = ['car', 'computer', 'apple', 'cat', 'phone']

kelime = input("Bir kelime girin: ")

if kelime not in turkce_kelimeler and kelime not in ingilizce_kelimeler:
    print("Geçersiz kelime!")
    exit()

harfler = list(kelime)

yenileri = []
for i in range(5):
    yeni_kelime = ''.join(random.sample(harfler, len(harfler)))
    if yeni_kelime in turkce_kelimeler or yeni_kelime in ingilizce_kelimeler:
        yenileri.append(yeni_kelime)

puanlar = []
for yeni_kelime in yenileri:
    uzunluk = len(yeni_kelime)
    zorluk = 1 if yeni_kelime in turkce_kelimeler else 2
    puanlar.append(uzunluk * zorluk)

print("Yeni kelimeler: ", yenileri)
print("Puanlar: ", puanlar)