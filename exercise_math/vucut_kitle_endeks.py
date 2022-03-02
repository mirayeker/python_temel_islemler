print("""
VUCUT KİTLE ENDEKSİ HESAPLAMA PROGRAMI 
BAKALIM SAĞLIKLI MISINIZ???""")
kilo=float(input("Lütfen kilonuzu girin: "))
boy=float(input("Lütfen boyunuzu girin: "))
indeks= kilo/ (boy** 2)
print("İndeks: {:.2f} ".format(indeks))
if(indeks<18.5):
    print("Zayıf")
elif(18.5<indeks and indeks<25):
    print("Normal")
elif(25<indeks and indeks<30):
    print("Fazla Kilolu")
else:
    print("Obez")