"""
Bir sayının basamaklarındaki tüm rakamların
ayrı ayrı küplerinin toplamı kendisine eşitse
bu sayıya Armstrong sayı denir.
Örneğin 153-> 1x10^2 + 5x10^1 + 3x10^0 =153
"""

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
    
else:
    print(sayı, "bir armstrong sayısı değildir.")
    