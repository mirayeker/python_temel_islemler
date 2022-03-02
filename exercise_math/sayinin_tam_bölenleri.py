def tam_bolen(sayi):
    tam_bolenler=[]

    for i in range(2,sayi):
        if(sayi%i==0):
            tam_bolenler.append(i)
    print("Sayinin tam bölenleri: ",tam_bolenler)
print("Çıkmak için 'q' ya basınız")
while True:
    sayi=input("Sayı:")
    if(sayi=="q"):
        print("İşlem sonlandırılıyor")
        break
    else:
        sayi=int(sayi)
        tam_bolen(sayi)
