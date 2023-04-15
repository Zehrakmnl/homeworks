"""Verilen a ve b iki tam sayisinin gcd(en büyük ortak bölen ) değerini hesaplayan platform bağimsiz bir gcd(a,b) fonksiyonu yaziniz. (40 puan)

Belirlenen bu gcd değerine göre: 

gcd(a,b) = ax + by 

ifadesini yazabilmek için x ve y değerlerini Öklid Algoritmasinin kullanarak bulunuz. (50 puan)

Son olarak gcd(a,b) = ax + by şeklinde yazilimini gösteriniz. (10 Puan)"""


#Verilen a ve b iki tam sayisinin gcd(en büyük ortak bölen ) değerini hesaplayan platform bağimsiz bir gcd(a,b) fonksiyonu yaziniz. (40 puan)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(36,-24)) # -12 çıktısını verecektir.

#gcd(a,b) = ax + by ifadesini yazabilmek için x ve y değerlerini Öklid Algoritmasinin kullanarak bulunuz. (50 puan)

def oklid(a, b):
    # Başlangıçta, a = 1x + 0y, b = 0x + 1y
    x, y = 1, 0
    ilk_x, ilk_y = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b

        # x ve y değerlerinin güncellenmesi
        x, ilk_x = ilk_x, x - q * ilk_x
        y, ilk_y = ilk_y, y - q * ilk_y

    return a, x, y

a = 36
b = -24

gcd, x, y = oklid(a, b)
print("gcd({}, {}) = {}*{} + {}*{}".format(a, b, gcd, x, a, y, b))
