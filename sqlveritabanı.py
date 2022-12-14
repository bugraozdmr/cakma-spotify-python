import sqlite3
class sarki():
    def __init__(self,isim,sanatci,album,sure):
        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.sure = sure
    def __str__(self):
        print(self.isim,self.sanatci,self.album,self.sure)
class spotify():
    def __init__(self):
        self.baglanti_kur()
    def baglanti_kur(self):
        self.baglan = sqlite3.connect("spotify.db")
        self.cursor = self.baglan.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sarki (isim TEXT,sanatci TEXT,album TEXT,sure INT)"
        self.cursor.execute(sorgu)
        self.baglan.commit()
    def baglanti_kes(self):
        self.baglan.close()
    def sarki_ekle(self,sarki):
        sorgu = "Insert into sarki values (?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sure))
        self.baglan.commit()
    def sarki_sil(self,isim):
        sorgu = "select * from sarki where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:             #arama yapıldı bundan ötürü listeye atandı.
            print("Böyle bir şarkı bulunamadı.")
        else:
            sorgu = "delete from sarki where isim = ?"
            self.cursor.execute(sorgu,(isim,))
            self.baglan.commit()
    def sarkilar(self):
        sorgu = "select * from sarki"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()
        for a,b,c,d in liste:
            print(a,b,c,d)
    def sarkı_guncelle(self,isim,yeni):
        sorgu = "select * from sarki where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Aranan şarkı bulunamadı.")
        else :
            sorgu = "update sarki set album = ? where isim = ?"
            self.cursor.execute(sorgu,(yeni,isim))
            self.baglan.commit()
    def totalsure(self):
        sorgu = "select sure from sarki"
        self.cursor.execute(sorgu)
        list = self.cursor.fetchall()
        a = 0
        for i in list:
            a += i[0]
        dk = a // 60
        sn = a%60
        print("{} dk {} sn".format(dk,sn))