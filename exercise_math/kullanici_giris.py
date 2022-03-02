print("""**************************
Kullanıcı girişi
******************************""")
sys_kullanici_adi= "mmiray"
sys_parola= "123456"
giris_hakki=3
while True:
    kullanici_adi=input("Kullanıcı adınızı giriniz: ")
    parola=input("Parolanızı giriniz: ")
    if (sys_kullanici_adi==kullanici_adi and sys_parola!=parola):
        print("Parolanız yanlış girdiniz!")
        giris_hakki -=1
    elif(sys_kullanici_adi!=kullanici_adi and sys_parola==parola):
        print("Kullanıcı adınızı yanlış girdiniz!")
        giris_hakki -=1
    elif(sys_kullanici_adi==kullanici_adi and sys_parola==parola):
        print("Başarıyla giriş yapıldı!")
        break
    if(giris_hakki==0):
        print("Giriş hakkınız bitmiştir!")
        break