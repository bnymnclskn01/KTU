# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:33:20 2021

@author: PC
"""
"""
sayi1=input("1. Sayı : ")
sayi2=input("2. Sayı : ")
sayi3=(float(sayi1)+float(sayi2))/2
print("Toplam :{0}".format(sayi3))
"""
"""
sayi=input("Sayı : ") Şartlama
if(int(sayi)<0): Şartlanma
    print("Sayı Negatif")
elif(int(sayi)>0): Şartlanma
    print("Sayı Pozitif")
else: Şartlanma
    print("Sayı Nötr")
"""
"""
yas= input("Yaşınız : ")
if(int(yas)<18): Şartlanma
    print("Yaş ehliyet almaya uygun değil")
else:
    print("Yaş ehliyet almaya uygun")
"""
"""
secim=input("Trafik var mı? V|Y")
if(secim=="Y"): Şartlama
    print("Okula otobüsle gideceğim")
else:
    print("Okula yürüyerek gidelim")
"""
""" Yenileyen Döngü
sayi=input("Sayı girin : ")
tekToplam=0
ciftToplam=0
for i in range(1, int(sayi)) :
    if(i%2==0):
        ciftToplam+=i
    else:
        tekToplam+=i
print("Tek Sayıların Toplamı :{0} ".format(tekToplam))
print("Çift Sayıların Toplamı :{0} ".format(ciftToplam))
"""

""" Tekrarlanan Döngü
from random import randint
rand=randint(1, 50)
sayac=0
while True:
    sayac+=1
    sayi=int(input("1 ile 50 arasında sayı giriniz : "))
    if(sayi==0 or sayi>50):
        print("Oyunu iptal ettiniz")
        break
    elif sayi<rand:
        print("Daha Yüksek Bir Sayı Giriniz : ")
        continue 
    elif sayi>rand:
        print("Daha düşük bir sayı giriniz. ")
        continue
    else :
        print("Rastgele seçilen sayı :{0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
"""
""" Yenilenen Döngü
def ArtikYil(yil):
    artik=False
    if yil%400==0 or(yil%4==0 and yil%100!=0):artik=True
    return artik
def YilinGunu(Ay,Gun,Yil):
    gunler=[31,28,31,30,31,30,31,30,31,30,31]
    if ArtikYil(Yil):
        gunler[1]=29
    sıra=0
    for a in range(Ay-1):
        sıra+=gunler[a]
    sıra+=Gun
    return sıra
print (YilinGunu(5,26,2000))
"""
"""
def ciftMi(x):
    return x%2==0
toplam=0
sayac=0
baslangic=input("Başlangıç Sayısı : ")
bitis =input("Bitis Sayısı : ")
for sayi in range(int(baslangic), int(bitis)+1): Yenilenen
    if(ciftMi(int(sayi))): Şartlanma
        toplam=toplam+sayi
        sayac=sayac+1
print("Ortalama ",(toplam/sayac))
Şeyma = Yenilenen | Şartlama
Serdar = Yenilenen | Şartlanma
Umut = Yenilenen | Şartlanma
Merve= Yenilenen | Şartlanma
Buse = Yenilenen | Şartlama
"""
"""
sayilar=[10,11,12,13,14,15,16,17,18,19,20]
for sayi in sayilar:
    if sayi%2!=0:
        print(sayi)
Merve= Yenilenen | Şartlama
Buse=  Yenilenen | Şartlanma
Umut=  Tekrar    | Şartlanma
Serdar=Tekrar    | Şartlama
Şeyma= Tekrar    | Şartlanma
Hamza= Tekrar    | Şartlama
"""
"""
for i in range(1,101):
    if i%3==0 or i%5==0:
        print(i)
Hamza Yenilenen|Şartlama
Şeyma Yenilenen|Şartlanma
Serdar Tekrar|Şartlanma
Umut Tekrar|Şartlanma
Buse Tekrar|Şartlama
Merve Tekrar|Şartlama
"""