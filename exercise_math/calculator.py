print("""*****************************
    Hesap Makinesi Programı 

Lütfen işlem seçiniz
1-Toplama İşlemi
2-Çıkarma İşlemi
3-Çarpma İşlemi
4-Bölme İşlemi

*********************************""")
a= int(input("birinci sayı giriniz"))
b= int(input("ikinci sayı giriniz"))
islem=input("İşlem numarasının giriniz: ")

if (islem=='1'):
    print("{} ile {} 'in toplamı {}" .format(a,b,a+b))
elif (islem=='2'):
    print("{} ile {} 'in farkı {}" .format(a,b,a-b))
elif (islem=='3'):
    print("{} ile {} 'in çarpımı {}" .format(a,b,a*b))
elif (islem=='4'):
    print("{} ile {} 'in bölümü {}" .format(a,b,a/b))
else:
    print("Geçersiz işlem!")