#TO DO LİST
import tkinter as tk

#yazdığımız seçili görevi çekeceğiz.
#
def gorev_ekle():
    yeni_gorev=gorev_giris.get()
    if yeni_gorev:
        gorevler.append({"gorev":yeni_gorev,"yapıldı":False}) #ekleme yaptıık
        gorev_listesi.insert(tk.END,yeni_gorev)
        gorev_giris.delete(0,tk.END)

def gorev_sil():
    secili_indeks=gorev_listesi.curselection() #curse in seçili olduğu alan
    if secili_indeks:  #eğer seçili indeksim ar ise herrhangi bir yer seçilmişse 
        gorevler.pop(secili_indeks[0])   #birden fazla eleman seçilirse pop yapıyor
        gorev_listesi.delete(secili_indeks)

def gorev_yapıldı():
    secili_indeks=gorev_listesi.curselection()
    if secili_indeks:
        gorevler[secili_indeks[0]]["yapıldı"]=True
        yeni_metin=gorevler[secili_indeks[0]]["gorev"]+"(YAPILDI)"
        gorev_listesi.delete(secili_indeks[0])
        gorev_listesi.insert(secili_indeks[0],yeni_metin)
        gorev_listesi.itemconfig(secili_indeks[0],fg="green")


gorevler=[]

#anapencere oluşturuyruz 
ana_pencere=tk.Tk()
ana_pencere.title("görev listesi")    #başlık yazdı 
 
#ana oencereden kullanıcıdan görev  alma inputu 
gorev_giris=tk.Entry(ana_pencere,width=40)
gorev_giris.pack(pady=5)
#görev ekleme butonu 
ekle_buton=tk.Button(ana_pencere,text="görev ekle",command=gorev_ekle)
ekle_buton.pack(pady=5)

#görev listesi alanını oluşturuyoruz.
gorev_listesi=tk.Listbox(ana_pencere,width=50,height=15)     #aldığım görevi listboxla sıralıyorum
gorev_listesi.pack(pady=10)

#seçile görebi silme butonnu olsuşturuyoruz
sil_buton=tk.Button(ana_pencere,text="seçilen görevi sil",command=gorev_sil)
sil_buton.pack(pady=5)

#yapıldı olarak işaretleme butonunu oluştuyoruz
yapildi_buton=tk.Button(ana_pencere,text="yapıldı olarak işaretle",command=gorev_yapıldı)
yapildi_buton.pack(pady=5)

#ana döngüyü başlat 
ana_pencere.mainloop()