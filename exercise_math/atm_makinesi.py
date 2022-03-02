print("""**********************
ATMA makinesine hoşgeldiniz
************************""")

print("\tİŞLEMLER")
print("""
1. Bakiye sorgulama
2. Para Çekme
3. Para Yatırma
program çıkmak için 'q' ya basınız.""")
bakiye=1000
while True:
    islem=input("İşlem seçiniz:")
    if(islem== 'q'):
        print("Yine bekleriz...")
        break
    elif(islem == '1'):
        print("bakiyeniz {} ".format(bakiye))
    elif(islem == '2'):
        miktar=int(input("Çekmek istediğiniz miktarı giriniz: "))
        if(bakiye - miktar < 0):
            print("Bakiye yetersiz!")
            continue
        bakiye -=miktar

    elif(islem == '3'):
        miktar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye += miktar



