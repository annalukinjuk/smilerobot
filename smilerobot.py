import numpy as np
from math import*
import matplotlib.pyplot as plt
from tkinter import *

#Создание проекта SMILEs

#Изучите примеры приведенные ниже.
#Изучите примеры приведенные ниже.
#Напишите программу содержащую список из Checkbutton(), расположенных в Frame() с названиями частей лица слева и Canvas() справа. На канве должны появляться части лица(https://www.tutorialspoint.com/python/tk_checkbutton.htm)
#Лицо состоит как минимум из 5 частей(овал лица, глаза, нос, рот ...)
#Выбирая необходимые части лица, их изображения должны появляться в канве, максимально заполняя ее.

#Окно 500X500
#Для рисования дуги arc(x1,y1,x2,y2,start,extent,fill):
from tkinter import * 

window=Tk() 
window.title("SMILe Robot")
#aken.iconbitmap('iconka.ico')
window.geometry('650x600')
f1=Frame(window,width=150,height=500)
f1.pack(side=LEFT)
c=Canvas(window, width=500, height=500, bg="pink") 
c.create_oval((5, 320, 100, 120),fill="yellow") # Овал
c.create_arc((5, 5, 50, 50), style=PIESLICE)# Сектор ("кусок пирога") 
c.create_arc((55, 5, 100, 50), style=ARC)# Дуга SMILE
#c.create_arc((105, 5, 150, 50), style=CHORD, start=0, extent=150, fill="blue") # от 0 до 150 градусов # Ломаная со стрелкой на конце 
c.create_line([(5, 55), (55, 55), (30, 95)], arrow=LAST) # Кривая (ломаная) 
c.create_line([(105, 55), (155, 55), (130, 95)], smooth=1) # Кривая (сглаженная) 
#c.create_polygon([(205, 55), (255, 55), (230, 95)], fill="green")# Многоугольник зеленого цвета 


#c.create_rectangle((105, 105, 150, 130), fill="red", outline="grey", width="5") # Прямоугольник красного цвета с большой серой границей 
#c.create_text((10, 410), text="FACE SMILE", anchor="nw") # Текст 
c.create_oval((5, 205, 6, 206), outline="red") # Эта точка визуально обозначает угол привязки 

c.create_text((105, 205), text="FACE SMILE", justify=LEFT, anchor="c") # Текст с заданным выравниванием 

c.create_oval((105, 205, 106, 206), outline="red") 
## Еще один вариант 
#c.create_text((205, 205), text="Hello,\nmy friend!", justify=CENTER, anchor="se") 
#c.create_oval((205, 205, 206, 206), outline="red") 
smile=Checkbutton(f1,text="smile",font="Calibri 16",bg="pink",var=1,onvalue=1, offvalue=0, height=5,width = 10)
nose=Checkbutton(f1,text="nose",font="Calibri 16",bg="pink",var=2,onvalue=1, offvalue=0, height=5,width = 10)
eye1=Checkbutton(f1,text="left eye",font="Calibri 16",bg="pink",var=3,onvalue=1, offvalue=0, height=5,width = 10)
eye2=Checkbutton(f1,text="right eye",font="Calibri 16",bg="pink",var=4,onvalue=1, offvalue=0, height=5,width = 10)
head=Checkbutton(f1,text="head",font="Calibri 16",bg="pink",var=5,onvalue=1, offvalue=0, height=5,width = 10)
var=IntVar()

smile.pack()
nose.pack()
eye1.pack()
eye2.pack()
head.pack()
c.pack(side=LEFT) 

window.mainloop() 

#В результате работы этой программы на экране появится окно:

#Пример 2

#from tkinter import *
#def kontroll():
#    lbl.configure(text=v.get())
#    if v.get()==1:
#        print("esmaspäev")
#    elif v.get()==2:
#        print("teisipäev")
#    #...
#win=Tk()
#win.title("Okno")
#win.geometry("200x200")
#v=IntVar()
#v.set(1)
#rad1=Radiobutton(win,text="Üks",variable=v,value=1,command=kontroll)
#rad2=Radiobutton(win,text="Kaks", variable=v,value=2,command=kontroll)
#lbl=Label(win, text="...")

#rad1.pack()

#rad2.pack()

#lbl.pack()

#win.mainloop()
