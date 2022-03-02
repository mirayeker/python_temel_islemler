liste1 = range(1,101)
liste2=list()
for i in liste1:
    if(i%2==0):
        liste2.append(i)
    else:
        continue
print("Çift sayılardan oluşan listemiz:\n",liste2)
#kısayol
print("**************************************")
liste= [x for x in range(1,101) if x%2==0]
print(liste[::-1])

