import tkinter as tk

#notları kaydederken diyoşog ekranı cıkmalı ve nereye kaydedeceğimizi secmeliyiz bir diyakog ekranına ihtiyacımız var  
from tkinter import filedialog

def not_ekle():
    yeni_not=not_giris.get("1.0",tk.END).strip()
    if yeni_not:
        notlar.append(yeni_not)
        not_listesi.insert(tk.END,yeni_not)
        not_giris.delete("1.0",tk.END)

def not_sil():
    secili_indeks=not_listesi.curselection()
    if secili_indeks:
        notlar.pop(secili_indeks[0])
        not_listesi.delete(secili_indeks)

def tum_notlari_temizle():
    notlar.clear()
    not_listesi.delete(0,tk.END)

 
def notlari_disari_aktar():
    dosya_yolu=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("metin dosyaları","*.txt")])
    if dosya_yolu:
        with open(dosya_yolu,"w",encoding="utf-8") as dosya:
            for not_metni in notlar:
                dosya.write(not_metni+"\n")
notlar=[]

#ana pencere oluşturuluyor
ana_pencere=tk.Tk()
ana_pencere.title("not alma uygulaması")

not_giris=tk.Text(ana_pencere,height=5,width=40)
not_giris.pack(pady=10)

ekle_buton=tk.Button(ana_pencere,text="not ekle",command=not_ekle)
ekle_buton.pack(pady=5)

not_listesi=tk.Listbox(ana_pencere,width=50,height=15)
not_listesi.pack(pady=10)

sil_buton=tk.Button(ana_pencere,text="sil",command=not_sil)
sil_buton.pack(pady=5)

temizle_buton=tk.Button(ana_pencere,text="tüm notları temizle",command=tum_notlari_temizle)
temizle_buton.pack(pady=5)

disari_aktar_buton=tk.Button(ana_pencere,text="tüm notları kaydet",command=notlari_disari_aktar)
disari_aktar_buton.pack(pady=5)

ana_pencere.mainloop()