"""
Mükemmel sayı, sayılar teorisinde,
kendisi hariç pozitif tam bölenlerinin toplamı
kendisine eşit olan sayı. Diğer bir ifadeyle,
bir mükemmel sayı, bütün pozitif tam bölenlerinin toplamının yarısına eşittir.
Örneğin 496
"""
#Kisa Kod:
def mukemmel_sayi(sayi):
   toplam=0
   for i in range(1,sayi):
       if(sayi%i==0):
           toplam +=i
   return toplam==sayi
for i in range(1,1001):
    if(mukemmel_sayi(i)):
        print("mükemmel sayi: ",i)


#Uzun sekilde yazarsak:
print("""
***************
Mükemmmel Sayi Bulma
çıkmak için '0' a basınız
****************""")
while True:
    sayi=int(input("Lütfen bir sayı giriniz:"))
    muko_sayi=0
    for i in range(sayi+1,0,-1):
        if(sayi%i==0):
         muko_sayi +=i
        elif(sayi%i !=0):
            continue
    if((muko_sayi-sayi)==sayi):
        print("Girmiş olduğunuz  {} sayısı mükemmeldir.".format(sayi))
    elif(sayi==0):
        print("Program sonlandırıldı.")
        break
    else:
        print("Gİrmiş olduğunuz {} sayı mükemmel değildir.".format(sayi))