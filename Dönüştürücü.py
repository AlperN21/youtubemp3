#Youtube video downloader -Alperen T.
from __future__ import unicode_literals
import youtube_dl #Youtube Download kütüphanesi.
import time
from colorama import init #Renk kütüphanesi
from colorama import Fore, Back, Style #Renk kütüphanesinin içindeki modüller
init()
print(Fore.WHITE)
sarki = input('Lütfen indirmek istediğiniz video url si--->') #Youtube da aratacağımız video adı
#Burada en önemli kısım mp4 istiyorsak ayarların içinin boş olması gerektiği çünkü boş olursa direk video yu indirir.
#O yüzden kullanıcıya mp3 mü istiyor mp4 mü sormamız lazım.
tür = input("mp3 mü istersiniz ? mp4 mü ? -ÖRN : mp3- ===>") #Kullanıcının ne istediğini soruyoruz.
if tür == "mp3" or "MP3": #Eğer mp3 ise
    print(Fore.GREEN) #yazımızı yeşil yapıyoruz
    print("mp3 seçildi!") #bir dönüt veriyoruz
    ayarlar = {
                 'format': 'bestaudio/best', #formatımızı ayarlıyoruz
                 'extractaudio' : True,  #ses dosyalarını almasını istiyoruz
                 'audioformat' : "mp3", #ses formatını mp3 yapıyoruz.
               }
    sonuc = "Müziğiniz" #sonuc için bir değişken atıyoruz.
elif tür == "MP4" or "mp4": #eğer mp4 derse
    print(Fore.GREEN) #yeşil yazı
    print("mp4 seçildi!") #dönüt
    ayarlar = {} #boş bırakıyoruz ki olduğu gibi alalım
    sonuc = "VİDEONUZ" #onuc için değişken
else:
    print(Fore.RED) #eğer hata çıkarsa
    print("Lütfen geçerli bir tür seçin!") #dönüt
    time.sleep(1) #okuması için zaman
    print("HATA KODU 10")#dönüt 2 kısa
    time.sleep(4) #süre
    exit() #çıkış
with youtube_dl.YoutubeDL(ayarlar) as ydl: #ydl olarak kısaltıyoruz
    ydl.download([sarki]) #indiriyoruz
print(Fore.CYAN)#cyan renk
print(Style.DIM) #kaln
print(sonuc+"Başarılı şekilde dönüştü ve indirmeye koyuldu!") #dönüt
time.sleep(2) #süre
print("-Alperen T")
time.sleep(0.3)