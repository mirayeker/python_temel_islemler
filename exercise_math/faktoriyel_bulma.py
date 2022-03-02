print("""********************
faktöriyel Bulma Programıı
**************************""")
print("Çıkmak için 'q' ya basınız"
      "faktoriyelini bulmak istediğiniz sayıyı giriniz:")
while True:
    sayi=input("Sayi: ")
    if(sayi == 'q'):
        print("programdan çıkıldı.")
        break
    else:
        sayi=int(sayi)

        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel *=i
        print("Girmiş oldugunuz {} sayısının faktoriyeli:  {}".format(sayi,faktoriyel))
