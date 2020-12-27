#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                    Final Proje                      #
#                Halil İbrahim Deniz                  #
#               halildeniz61@gmail.com                #      
#######################################################

import time

print("           Öğrenci Otomasyon Giriş Sayfası    ")
time.sleep(1)
print("   Giriş yapmak için lütfen adınızı ve soyadınızı giriniz.")
time.sleep(1)

d = {"isim":"Halil", "soyisim":"Deniz" }
d1= {"arasinav": 38, "final": 66, "proje": 89}
check=False
ders_listesi=[]
secilen_dersler=[]

def ders_secimi(ders_sayisi):

            if (0<ders_sayisi<3):
                    print("Kayıt olabilmek için, ders listesinden az 3 ders seçmek zorundasınız.")

            elif (3 <=ders_sayisi <=5):

                for i in range(0,ders_sayisi):
                    sec_ders=input(f'Seçmek istediğiniz {i+1}. dersin adını giriniz: ').title()

                    if (sec_ders in ders_listesi):
                        secilen_dersler.append(sec_ders)
                      
                    elif(ders_sayisi!=len(secilen_dersler) or len(secilen_dersler<3)):
                        print("Seçmek istediğiniz ders sayısı ile seçinlen ders listesindeki ders sayısı eşleşmemektedir. Ders seçimlerini tekrar kontrol ediniz")
                        #eklenek_ders = input(f'Seçmek istediğiniz {i+1}. dersin adını giriniz: ').title()
            else:
                print("Böyle bir seçim yapılamaz.")
            
            ders_adi = input("Sınava girmek istediğiniz dersin adını giriniz: ").title()

            grade=float(d1["arasinav"]*0.3+(d1["final"]*0.5)+d1["proje"]*0.2)
                        
            if (90<=grade<=100):
                print(f'Yılsonu notunuz: {grade}. {ders_adi} dersini AA ile geçtiniz.')
            elif (70<=grade<90):
                print(f'Yılsonu notunuz: {grade}. {ders_adi} dersini BB ile geçtiniz.')
            elif (50<=grade<70):
                print(f'Yılsonu notunuz: {grade}. {ders_adi} dersini CC ile geçtiniz.')
            elif (30<=grade<50):
                print(f'Yılsonu notunuz: {grade}. {ders_adi} dersini DD ile geçtiniz.')
            else:
                print(f'Yılsonu notunuz: {grade}. {ders_adi} dersinden FF aldınız ve Başarısız Oldunuz.')
            return


for i in range(3):
    k_adi =input("   Adı: ").title()
    k_soyadi= input("Soyadı: ").title()

    if (d["isim"] == k_adi and d["soyisim"] == k_soyadi):
        print("Tebrikler, Başarıyla giriş yaptınız.")
        time.sleep(1)
        print("          Hoşgeldiniz                ")

        time.sleep(3)
        print("   Lütfen 5 tane ders adı giriniz: ")
        time.sleep(1)


        for i in range(1,6):

            ders=input(f'{i}. ders adını giriniz: ').title()
            ders_listesi.append(ders)
        #print(ders_listesi)

        time.sleep(1)
           
        ders_sayisi = int(input("Seçmek istediğinin ders sayısını giriniz: "))
        time.sleep(1)

            
        ders_secimi(ders_sayisi)            
        check = True
        break

    elif (d["isim"] == k_adi and d["soyisim"] != k_soyadi):
        print("Soyadınızı yanlış girdiniz.")

    elif (d["isim"] != k_adi and d["soyisim"] == k_soyadi):
        print("Adınızı yanlış girdiniz.")

    else:
        print("Adınızı ve soyadınızı yanlış girdiniz.")

if not check:
    print("3 kez deneme hakkınız doldu. Lütfen daha sonra tekrar deneyiniz. ")
     