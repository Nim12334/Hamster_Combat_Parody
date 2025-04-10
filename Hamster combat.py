from PIL import Image
from customtkinter import*
import customtkinter as ctk
from random import*
import numpy as np
import time
import tkinter.messagebox as mg
import tkinter
from threading import Thread
ct=ctk.CTk()
ct.title("Hamster Combat 0.8-e-alfa-c")
ct.iconbitmap("avatar.ico")
ctk.set_appearance_mode('dark')
bw=0
bw1=str(bw)
bw3=0
bw2=str(bw3)
bw4=0
bw5=str(bw4)
vb4=0
vb5=str(vb4)
n=0
n1=str(n)
n2=0
n3=str(n2)
n5=0
n4=str(n5)
z12=0
z1=str(z12)
g1=0
g2=str(g1)
grivny=0
grivny1=str(grivny)
bitcoin=0
bitcoin1=str(bitcoin)
fynt=0
fynt1=str(fynt)
lira=0
lira1=str(lira)
etherium1=0
etherium2=str(etherium1)

image_open = CTkImage(light_image=Image.open('image1.jpg'), size=(400, 400))
image_open1 = CTkImage(light_image=Image.open('hamsterone.gif'), size=(400, 400))
image_open2 = CTkImage(light_image=Image.open('Hamster.jpg'), size=(400, 400))
image_open3 = CTkImage(light_image=Image.open('hamsterc.jfif'), size=(400, 400))
image_open4 = CTkImage(light_image=Image.open('jop.png'), size=(400, 400))
image_open5 = CTkImage(light_image=Image.open('H.jpg'), size=(400, 400))
image_open25 = CTkImage(light_image=Image.open('images.jpg'), size=(40, 40))
image_open6 = CTkImage(light_image=Image.open('krytoi.jpeg'), size=(400, 400))
image_open7 = CTkImage(light_image=Image.open('krytoi1.jpg'), size=(400, 400))
image_open8 = CTkImage(light_image=Image.open('homak.jpg'), size=(400, 400))
image_open50 = CTkImage(light_image=Image.open('MONEY.jpg'), size=(400, 400))
image_openfynt = CTkImage(light_image=Image.open('hamfoot.jpg'), size=(50, 50))
image_openlira = CTkImage(light_image=Image.open('lira.jpg'), size=(50, 50))

l=ctk.CTkLabel(master=ct,text="0",text_color="white",font=(ct,30))
l1=ctk.CTkLabel(master=ct,text="$:"+bw1,text_color="green",font=(ct,30))
l2=ctk.CTkLabel(master=ct,text="Br:"+bw2,text_color="green",font=(ct,30))
l3=ctk.CTkLabel(master=ct,text="₽:"+bw5,text_color="green",font=(ct,30))
l4=ctk.CTkLabel(master=ct,text="€:"+vb5,text_color="green",font=(ct,30))
l5=ctk.CTkLabel(master=ct,text="di:"+n1,text_color="blue",font=(ct,30))
l6=ctk.CTkLabel(master=ct,text="¥:"+n3,text_color="red",font=(ct,30))
l7=ctk.CTkLabel(master=ct,text="₸:"+n4,text_color="yellow",font=(ct,30))
l8=ctk.CTkLabel(master=ct,text="zł:"+z1,text_color="#002F55",font=(ct,30))
l11=ctk.CTkLabel(master=ct,text=f"coin:{g2}",text_color="yellow",font=(ct,30))
l111=ctk.CTkLabel(master=ct,text=f"₴:{grivny1}",font=(ct,30))
l112=ctk.CTkLabel(master=ct,text=f" £:{fynt1}",font=(ct,30),text_color="purple")
l113=ctk.CTkLabel(master=ct,text=f" ₺:{lira1}",font=(ct,30),text_color="orange")
etherium=ctk.CTkLabel(master=ct,text=f"♦:{etherium2}",text_color="green",font=(ct,30))
def com_eteth():
    global etherium1
    global g1
    global b
    m22=randint(1,50)
    if etherium1>=1:
     etherium1-=1
     g1+=5000
     g3=str(g1)
     etherium.configure(text=f"♦:{etherium2}")
     l11.configure(text=f"coin:{g3}")
    if m22==9:
        b+=0.5
        l.configure(text=b)
    print(m22)
    

etheriumn=ctk.CTkButton(master=ct,text=f"♦ перавести в coin",text_color="white",fg_color="green",font=(ct,30),command=com_eteth)

time1=0
bitcoin_true=0
etherium_true=0




combobox=CTkLabel(ct,text=f"",font=(ct,30))
def Hi():
    while (True):
     time.sleep(1)
     global time1
     time1+=1
     combobox.configure(text=f"Время:{time1}")



b=0
b1=0
z=1
coin=0.1



def asc():
    global b
    global g1
    b+=z
    g1+=coin
    g2=(str(g1))
    b1=str(b)
    l.configure(text=b1)
    l11.configure(text=f"coin:{g2}")
    if b>=10 and b>50:


        v.configure(image=image_open1)
    if b>=100 and b>100:
        v.configure(image=image_open2)
    if b>=200 and b>200:
        v.configure(image=image_open6)
    if b>=300 and b>300:
        v.configure(image=image_open7)
    if b>=400 and b>400:
        v.configure(image=image_open3)
    if b>=500 and b>500:
        v.configure(image=image_open4)
    if b>=600 and b>600:
        v.configure(image=image_open5)
    if b>=700 and b>700:
        v.configure(image=image_open8)
    if b>=800 and b>800:
        v.configure(image=image_open50)
def autoclicer():
    global grivny
    global b3
    global b
    b99 = b / 100
    grivny += b99
    b-=b
    l.configure(text=b)

    bw1=str(grivny)
    l111.configure(text="₴:"+bw1)
     
  
 
l12=ctk.CTkButton(master=ct,image=image_open25,text="",fg_color="yellow",font=(ct,30),command=autoclicer)


def asc1():
    global bw3
    global b3
    global b
    b3 = b / 1656
    bw3 += b3
    b-=b
    l.configure(text=b)

    bw1=str(bw3)
    l1.configure(text="$:"+bw1)
def c():
    global bw4
    global b3
    global b
    b4= b / 45
    bw4 += b4
    b-=b
    l.configure(text=b)
    bw1=str(bw4)
    l2.configure(text="Br:"+bw1)

def c1():
    global bw
    global bw4
    global b
    b4= b / 2
    bw += b4
    b-=b
    l.configure(text=b)
    bw1=str(bw)
    l3.configure(text="₽:"+bw1)
def c2():
    global bw
    global vb4
    global b
    b4= b / 10
    vb4 += b4
    b-=b
    l.configure(text=b)
    bw1=str(vb4)
    l4.configure(text="€:"+bw1)
def bitcointranslate():
    global bitcoin
    global g1
    global b
    tran=bitcoin*10000
    if bitcoin>=1:
     bitcoin-=bitcoin
     g1+=tran
    l11.configure(text=f"coin:{g1}")
    bitcoinvalut.configure(text=f"₿:{bitcoin}")
    valut=randint(1,100)
    print(valut)

    if valut==15:
        b+=1
        l.configure(text=b)
    
bitcoin1val=CTkButton(master=ct,text=f"Перевести в coin",fg_color="green",hover=True,text_color="yellow",command=bitcointranslate,font=(ct,30))

    
def c12():
    global bw
    global n
    global b
    global bitcoin_true
    b4= b / 500
    n += b4
    b-=b
    l.configure(text=b)
    bw1=str(n)
    l5.configure(text="di:"+bw1)
    n11=randint(0,100)
    print(n11)
   
  
    
    if n11==35 and bitcoin_true==0:
        global bitcoin
        global etherium_true
        etherium_true+=1
        bitcoin+=1
        print(etherium_true)
        bitcoinvalut.configure(text=f"₿:{bitcoin}")
        bitcoinvalut.place(x=1,y=510)
        bitcoin1val.place(x=1,y=550)
    if n11==7 and etherium_true==0:
        global etherium1
        bitcoin_true+=1
        etherium1+=1
        print(bitcoin_true)
        etherium.configure(text=f"♦:{etherium1}",font=(ct,30))
        etherium.place(x=1,y=510)
        etheriumn.place(x=1,y=550)
bitcoinvalut=CTkLabel(master=ct,text=f"₿:{bitcoin}",font=(ct,30))
    

def c13():
    global bw
    global n2
    global b
    rand1=randint(1,100)
    print(rand1)
    b4= b / 5
    n2 += b4
    b-=b
    l.configure(text=b)
    bw1=str(n2)
    l6.configure(text="¥:"+bw1)
    if rand1==75:
        Thread(target = Hi).start()
       
  
    
def we():
    global b
    r=randint(1,2)
    if r==1:
        b/=2
    if r==2:
        b= b*2
    l.configure(text=b)
def we2():
    global z
    global n
    global g1
    global n1
    global g2
    global g1
    global bitcoin
    global bitcoin1
 
    if  n>=1 and g1>=2000:
        n -= 1
        z*=2
        g1-=2000
        g2=str(g1)
        n1=str(n)
    l5.configure(text="di:" + n1)
    l11.configure(text=f"coin:{g2}")
    if n>=0:
        pass
    if g1<2000:
        mg.askokcancel("У вас недостаточна","coin")
   
    
    
    


def we3():
    global bw
    global n5
    global b
    b4= b / 35
    n5 += b4
    b-=b
    l.configure(text=b)
    bw1=str(n5)
    l7.configure(text="₸:"+bw1)
def we4():
    global bw
    global z12
    global b
    b4= b / 35
    z12 += b4
    b-=b
    l.configure(text=b)
    bw1=str(z12)
    l8.configure(text="zł:"+bw1)
def com1():
    global bw
    global fynt
    global b
    b4= b / 150
    fynt+= b4
    b-=b
    l.configure(text=b)
    bw1=str(fynt)
    l112.configure(text="£:"+bw1)
def com2():
    global bw
    global lira
    global b
    b4= b /1.5
    lira+= b4
    b-=b
    l.configure(text=b)
    bw1=str(lira)
    l113.configure(text="₺:"+bw1)


image6=CTkImage(light_image=Image.open('yan.jfif'),size=(50,50))

image2=CTkImage(light_image=Image.open('dollor.jfif'),size=(50,50))
image1=CTkImage(light_image=Image.open('oi.jfif'),size=(50,50))
image3=CTkImage(light_image=Image.open('images.jfif'),size=(50,50))
image4=CTkImage(light_image=Image.open('eura.jfif'),size=(50,50))
image5=CTkImage(light_image=Image.open('Без названия.jfif'),size=(50,50))
image7=CTkImage(light_image=Image.open('images.png'),size=(50,50))
image8=CTkImage(light_image=Image.open('zlota.jpg'),size=(50,50))
def common3():
    global b,g1
    g3=g1
    g5=(g3/10)
    l.configure(text=f"{b+g5}")
    b+=g5
    g1=0
    l11.configure(text="coin:0")


v=CTkButton(master=ct,text="",image=image_open,fg_color='green',hover_color='green',hover=True,command=asc)
v1=CTkButton(master=ct,text="",fg_color="green",image=image2,hover=True,command=asc1)
v2=CTkButton(master=ct,text="",fg_color="blue",image=image1,hover=True,command=c)
v3=CTkButton(master=ct,text="",fg_color="red",image=image3,hover=True,command=c1)
v4=CTkButton(master=ct,text="",fg_color="yellow",image=image4,hover=True,command=c2)
v5=CTkButton(master=ct,text="",image=image5,fg_color="blue",hover=True,command=c12)
v6=CTkButton(master=ct,text="",image=image6,fg_color="red",hover=True,command=c13)
v7=CTkButton(master=ct,text="50/50",fg_color="black",hover=True,command=we,font=(ct,50))
v9=CTkButton(master=ct,text="*2=1 алмаз",fg_color="yellow",hover=True,command=we2,font=(ct,50))
v10=CTkButton(master=ct,text="",image=image7,fg_color="yellow",hover=True,command=we3,font=(ct,50))
v11=CTkButton(master=ct,text="",image=image8,fg_color="#002F55",hover=True,command=we4,font=(ct,50))
vfoont=CTkButton(master=ct,text="",image=image_openfynt,fg_color="purple",command=com1,hover=True,font=(ct,50))
vlira=CTkButton(master=ct,text="",image=image_openlira,fg_color="orange",command=com2,hover=True,font=(ct,50))
vlira1=CTkButton(master=ct,text="10 coin=1",fg_color="orange",command=common3,hover=True,font=(ct,50))
v.place(x=450,y=100)
v1.place(x=1220,y=0)
v2.place(x=1220,y=100)
v3.place(x=1220,y=200)
v4.place(x=1220,y=300)
v5.place(x=1220,y=400)
v6.place(x=1220,y=500)
v7.place(x=1220,y=600)
vfoont.place(x=950,y=250)
vlira.place(x=950,y=350)
vlira1.place(x=950,y=450)
v9.place(x=0,y=600)
v10.place(x=950,y=0)
v11.place(x=950,y=90)
l.place(x=660,y=0)
l1.place(x=7,y=0)
l2.place(x=7,y=50)
l3.place(x=7,y=100)
l4.place(x=7,y=150)
l5.place(x=7,y=200)
l6.place(x=7,y=250)
l7.place(x=7,y=300)
l8.place(x=7,y=350)
l111.place(x=1,y=390)
l11.place(x=660,y=30)
l12.place(x=950,y=180)
l112.place(x=0,y=430)
l113.place(x=0,y=470)
combobox.place(x=100,y=1)
ct.mainloop()