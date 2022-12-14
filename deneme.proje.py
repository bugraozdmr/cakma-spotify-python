from sqlveritabanı import *
print("ÇAKMA SPOTİFY\n")
spotify1 = spotify()
print("1.Şarkı ekle\n2.Şarkı sil\n3.Şarkı listesi\n4.Şarkı Güncelle\n5.Toplam Liste Süresi\n6.Çıkış\n\n\n")
while True:
    secim = int(input("seçim :"))
    match secim:
        case 1:
            isim = input("şarkı adı :")
            sanatci = input("şarkıyı kim söylüyor :")
            album = input("şarkı hangi albüme ait :")
            sure = int(input("şarkı süresi (saniye):"))
            sarki1 = sarki(isim,sanatci,album,sure)
            spotify1.sarki_ekle(sarki1)
        case 2:
            isim = input("silinecek şarkı ismi :")
            spotify1.sarki_sil(isim)
        case 3:
            spotify1.sarkilar()
        case 4:
            isim = input("hangi şarkıyı güncelleyeceksin :")
            yeni = input("yeni değeri :")
            spotify1.sarkı_guncelle(isim,yeni)
        case 5:
            spotify1.totalsure()
        case 6:
            print("Çıkış yapılıyor.")
            exit(1)
        case _:
            print("Geçersiz değer !")