import tkinter as tk
from tkinter import filedialog
# resmi bir canvas içrisine alacağız  
from tkinter import Canvas,PhotoImage,colorchooser
from PIL import Image,ImageTk,ImageDraw,ImageOps,ImageFont

def resim_yukle():
    dosya_yolu=filedialog.asksaveasfilename(filetypes=[("resim dosyaları","*jpg;*jpeg;*.png")])
    if dosya_yolu:
        global resim,duzenlenmis_resim,cizim
        resim=Image.open(dosya_yolu)
        duzenlenmis_resim=resim.copy()
        cizim=ImageDraw.Draw(duzenlenmis_resim)
        guncelle_canvas()

def guncelle_canvas():
    global Canvas_resim
    tk_resim=ImageTk.PhotoImage(duzenlenmis_resim)
    Canvas_resim=tk_resim
    Canvas.create_image(0,0, anchor=tk.NW,Image=tk_resim)
    Canvas.config(scrollregion=Canvas.bbox(tk.ALL))

def siyah_beyaz_yap():
    global duzenlenmis_resim,cizim
    if duzenlenmis_resim:
        duzenlenmis_resim=ImageOps.grayscale(duzenlenmis_resim).convert("RGB")
        cizim =ImageDraw.Draw(duzenlenmis_resim)
        guncelle_canvas()

def yazi_ekle(event):
    if duzenlenmis_resim:
        yazi=yazi_giris.get()
        if yazi:
            x,y=Canvas.canvasx(event.x),Canvas.canvasy(event.y)
            font=ImageFont.truetype("arial.ttf",yazi_boyut)
            cizim.text((x,y),yazi,fill=yazi_renk,font=font)
            guncelle_canvas()
def yazi_rengi_degistir():
    global yazi_renk
    secilen_renk=colorchooser.askcolor(title="yazı rengi seç",)[1]
    if secilen_renk:
        yazi_renk=secilen_renk

def ciz():
    if duzenlenmis_resim:
        Canvas.bind("<B1-Motion>",cizim_yap)
def cizim_yap():
    global cizim
    x,y=Canvas.canvasx(event.x),Canvas.canvasy(event.y)
    cizim.ellipse((x-2,y-2,x+2,y+2),fill=kalem_renk,outline=kalem_renk)
    guncelle_canvas()

def kalem_rengi_degistir():
    global kalem_renk
    secilen_renk=colorchooser.askcolor(title="kalem rengi seç")[1]
    if secilen_renk:
        kalem_renk=secilen_renk


def resmi_kaydet():
    dosya_yolu=filedialog.asksaveasfilename(defaultextension=".png",filetypes=["png dosyası","*.png"])
#global değişkenler oluştucağız 
resim=None
cizim=None
duzenlenmis_resim=None
Canvas_resim=None
yazi_renk="red"
yazi_boyut=20
kalem_renk="blue"

ana_pencere=tk.Tk()
ana_pencere.title("resim düzenleyici")

arac_cercevesi=tk.Frame(ana_pencere)
arac_cercevesi.pack(side=tk.LEFT,fill=tk.Y,padx=10,pady=10)

yukle_buton=tk.Button(arac_cercevesi,text="resim yükle",command=resim_yukle)
yukle_buton.pack(pady=5)

siyah_beyaz_buton=tk.Button(arac_cercevesi,text="siyah beyaz yap",command=siyah_beyaz_yap)
siyah_beyaz_buton.pack(pady=5)

yazi_giris=tk.Entry(arac_cercevesi,width=20)
yazi_giris.pack(pady=5)
yazı_ekle_label=tk.Label(arac_cercevesi,text="yazıyı eklemek için resme tıklayınız")  #abel sadece metin barındıran bir araç
yazı_ekle_label.pack()

yazi_renk_button=tk.Button(arac_cercevesi,text="yazı rengi seç",command=yazi_rengi_degistir)
yazi_renk_button.pack(pady=5)

ciz_buton=tk.Button(arac_cercevesi,text="çizim yap",command=ciz)
ciz_buton.pack(pady=5)

kalem_renk_buton=tk.Button(arac_cercevesi,text="kalem rengi değiştir",command=kalem_rengi_degistir)
kalem_renk_buton.pack(pady=5)

kaydet_buton=tk.Button(arac_cercevesi,text="resmi kaydet",command=resmi_kaydet)
kaydet_buton.pack(pady=5)

Canvas=Canvas(ana_pencere,bg="white",width=600,height=400,scrollregion=(0,0,1000,1000))
Canvas.pack(side=tk.RIGHT,expand=True,fill=tk.BOTH)

Canvas.bind("<Button-1>",yazi_ekle)
ana_pencere.mainloop()