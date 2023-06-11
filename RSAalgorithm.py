"""
Oluşturduğumuz algoritmanın aşamaları

    1. p ve q değerleri belirlenir. (101,103) ikisi de asal sayı olması istenir.
    2. n değeri hesaplanır (10.403) -> n = p*q
    3. Totient Fonksiyonu uygulanır => 10.200 (kendilerinden küçük tam bölenlerin sayısı)
    4. (private key) e sayısı hesaplanır. 1 ile totient fonk arasında bir değer olmalı. Totient fonk ile asal bir değer olmalı
    5. d sayısı hesaplanır. d sayısı özel olarak saklanır. bu d sayısı EXTEND EUCLID ile hesaplanır.
    !! e ve d aralarında asal olmalıdır. ikisinden biri gizli olmalı.

        public anahtarlar -> n , e   ::: karşı taraf bunları bilmeli
        private değerler -> totient fonk, d ::: bu değerler gizli olarak tutulur.
        private anahtar -> d*e = 1(mod(totient fonk.)) -> e'yi belirledikten sonra d böyle hesaplanıyor.

        e = 37 olsun o zaman d =  34000  olarak hesaplanır
        d*e = 1(mod(totient fonk.)) formülünden  33d = 10200k + 1 hesabı yapılacaktır. k 10 olursa d 34000 olarak bulunmaktadır.

    Şifreleme
        c = (message)^e mod n

    Şifrenin Açılması
        m = c^d mod n
"""
import math

def setkeys():
    global public_key, private_key,n
    asal1 = 101;asal2 = 103

    n = (asal1 * asal2)
    ti = (asal1 - 1) * (asal2 - 1)

    e = 37
    public_key = e
    #print(e)

    # d = (k*Φ(n) + 1) / e
    d = 9373
    private_key = d
    #print(d)

def encrypt(message):
    #c = (message)^e mod n
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        e -= 1
    return encrypted_text % n

def decrypt(message):
    # m = c^d mod n
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= message
        d -= 1
    return decrypted % n

# Karakter <=> ACII encoder ve decoder ile çeviriliyor
def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s
if __name__ == '__main__':
    setkeys()
    procces = input ("Yapmak istediğiniz işlem nedir ? encryption(0), decryption(1) ")
    text = input ("Metni giriniz: ")
    coded = encoder(text)
    if procces == '0':
        print("\nThe encoded message")
        print(''.join(str(p) for p in encoder(text)))
    elif procces == '1':
        print("\nThe decoded message\n")
        print(''.join(str(p) for p in decoder(coded))+'\n ')
    else :
        print("!!!!!! \nLütfen programı tekrar başaltıp geçerli bir işlem numarası giriniz. ")
