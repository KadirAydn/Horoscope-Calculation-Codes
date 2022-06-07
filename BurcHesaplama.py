from ast import Break
from traceback import print_tb


print("BURÇ HESAPLAMA UYGULAMASINA HOŞGELDİNİZ! \n")


try:
    ay = int(input("Kaçıncı ayda doğdun: "))
except ValueError:
    print("HATA - BİR SAYI GİRMELİSİNİZ")
    quit()

if ay == 1:
    print("Demek Ocak ayında doğdun")
    try:
        gun = int(input("Ocak ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # OCAK AYI #
        print("OĞLAK BURCUSUN")
    elif 20 < gun < 32:
        print("KOVA BURCUSUN")
        


elif ay == 2:
    print("Demek Şubat ayında doğdun")
    try:
        gun = int(input("Şubat ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 29:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 20:                                        # ŞUBAT AYI #
        print("KOVA BURCUSUN")
    elif 19 < gun < 30:
        print("BALIK BURCUSUN")
        


elif ay == 3:
    print("Demek Mart ayında doğdun")
    try:
        gun = int(input("Mart ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # MART AYI #
        print("BALIK BURCUSUN")
    elif 20 < gun < 32:
        print("KOÇ BURCUSUN")




elif ay == 4:
    print("Demek Nisan ayında doğdun")
    try:
        gun = int(input("Nisan ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # NİSAN AYI #
        print("KOÇ BURCUSUN")
    elif 20 < gun < 31:
        print("BOĞA BURCUSUN")



elif ay == 5:
    print("Demek Mayıs ayında doğdun")
    try:
        gun = int(input("Mayıs ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 21:                                        # MAYIS AYI #
        print("BOĞA BURCUSUN")
    elif 20 < gun < 32:
        print("İKİZLER BURCUSUN")



elif ay == 6:
    print("Demek Haziran ayında doğdun")
    try:
        gun = int(input("Haziran ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 22:                                        # HAZİRAN AYI #
        print("İKİZLER BURCUSUN")
    elif 21 < gun < 31:
        print("YENGEÇ BURCUSUN")




elif ay == 7:
    print("Demek Temmuz ayında doğdun")
    try:
        gun = int(input("Temmuz ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 23:                                        # TEMMUZ AYI #
        print("YENGEÇ BURCUSUN")
    elif 22 < gun < 32:
        print("ASLAN BURCUSUN")




elif ay == 8:
    print("Demek Ağustos ayında doğdun")
    try:
        gun = int(input("Ağustos ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # AĞUSTOS AYI #
        print("ASLAN BURCUSUN")
    elif 23 < gun < 32:
        print("BAŞAK BURCUSUN") 





elif ay == 9:
    print("Demek Eylül ayında doğdun")
    try:
        gun = int(input("Eylül ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # EYLÜL AYI #
        print("BAŞAK BURCUSUN")
    elif 23 < gun < 31:
        print("TERAZİ BURCUSUN")




elif ay == 10:
    print("Demek Ekim ayında doğdun")
    try:
        gun = int(input("Ekim ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 24:                                        # EKİM AYI #
        print("TERAZİ BURCUSUN")
    elif 23 < gun < 32:
        print("AKREP BURCUSUN")





elif ay == 11:
    print("Demek Kasım ayında doğdun")
    try:
        gun = int(input("Kasım ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 30:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 23:                                        # KASIM AYI #
        print("AKREP BURCUSUN")
    elif 22 < gun < 31:
        print("YAY BURCUSUN")





elif ay == 12:
    print("Demek Aralık ayında doğdun")
    try:
        gun = int(input("Aralık ayının kaçında doğdun: "))
    except ValueError:
        print("HATA - BİR SAYI GİRMELİSİNİZ")
        quit()
    if gun < 1 or gun > 31:
            print("HATA - GEÇERLİ BİR GÜN GİRMEDİNİZ")
    if 0 < gun < 22:                                        # ARALIK AYI #
        print("YAY BURCUSUN")
    elif 21 < gun < 32:
        print("OĞLAK BURCUSUN")





else:
    print(ay,"yazdınız.Lütfen tekrar deneyin ve 1-12 aralığında sayı girin")
    exit()

# coded by Kadir Aydın #
# insta: _kadiraydnn_