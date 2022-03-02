print("********"
      "Geometrik şekil hesaplama"
      "********")
print("Hangi geometrik şeklin tipini bulmak istiyorsunuz: ")
print("1-Üçgen\n"
      "2-Dikdortgen")
secim=input("İşleminiz: ")
if (secim=='1'):
    print("Lütfen üçgenin kenarlarını giriniz:")
    a=int(input("Birinci kenar: "))
    b=int(input("İkinci kenar: "))
    c=int(input("Üçüncü kenar: "))
    if (abs(a-b)<c and c <abs(a+b)) or (abs(a-c)<b and b<abs(a+c)) or (abs(b-c)<a and a<abs(b+c)):
        #abs(a+b) > c and abs(a+c) > b and abs(b+c) > a hoca bu şekilde yazmış
        if (a == b and b == c):
            print("Üçgeninizin tipi eşkenar.")
        elif (a == b or a == c):
            print("üçgeninizin tipi ikizkenar.")
        else:
            print("Sıradan bir üçgen")

    else:
        print("Girdiğiniz değerlerle herhangi bir üçgen oluşturulamıyor!")

elif (secim=='2'):
    print("Lütfen dörtgenin kenarlarını giriniz:")
    a = int(input("Birinci kenar: "))
    b = int(input("İkinci kenar: "))
    c = int(input("Üçüncü kenar: "))
    d = int(input("Dördüncü kenar: "))
    if(a==b and b==c and c==d):
        print("Dörtgeninizin tipi karedir")
    elif (a==c and b==d):
        print("Dörtgeninizin tipi dikdörtgendir")
    else:
        print("Dörtgeninizin tipi sıradan dörtgendir.")
else:
    print("Geçersiz seçim!")