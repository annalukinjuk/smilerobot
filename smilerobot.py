
from tkinter import*

head=""
def add_head():
	global c, head
	if var_head.get()==1:
		head=c.create_oval((150,400, 400, 50),fill="brown",outline="black")
	else:
		
		
def add_nose():
	global c
	if var_nose.get()=="nose":
		c.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")
	else:
		c.delete(ALL)
ulqba=""
def add_smile():
	global ulqba
	if var_mouth.get()=="smile":
		a=c.create_line((213, 215, 90, 215),fill="black",width=3)
	else:
		c.delete(ulqba)







b=c=d=e=""
def Eyes():
	global b,c,d,e
	if var_eyes.get()=="глаза":
		b=c.create_oval((72,72,130,130),fill="white")
		c=c.create_oval((165,72,221,130),fill="white")
		d=c.create_oval((82,82,117,120),fill="black")
		e=c.create_oval((175,82,211,120),fill="black")
	else:
		cdelete(b,c,d,e)
a1=a2=a3=a4=a5=a6=a7=a8=a9=a10=a11=a12=""




#def add_nose():
#    if var_nose.get()=="nose":
#        lbl.configure(text="add a nose on canvas")
#    else: 
#        lbl.configure(text="need to remove the nose")
#def add_smile():
#    if var_smile.get()=="smile":
#        vastus.configure(text="add smile on canvas")
#    else:
#        vastus.configure(text="need to remove smile")
#        draw.destroy
#def add_head():
#    if var_head.get()=="head":
#        c.create_oval((150,400, 400, 50),fill="brown")#Овал IDEALNO1111 NE MENYAT NI4EGO!!!!!!!!
root=Tk() 
root.title("SMILe Robot")
#aken.iconbitmap('iconka.ico')
root.geometry('650x600')
f1=Frame(root,width=150,height=500)
f1.pack(side=LEFT)
c=Canvas(root, width=500, height=500, bg="pink") 
c.create_arc((100, 5, 100, 100), style=PIESLICE, extent=180)# Сектор ("кусок пирога") 
c.create_arc((55, 5, 100, 50), style=ARC)# Дуга SMILE
#c.create_arc((105, 5, 150, 50), style=CHORD, start=0, extent=150, fill="blue") # от 0 до 150 градусов # Ломаная со стрелкой на конце 
c.create_line([(5, 55), (55, 55), (30, 95)], arrow=LAST) # Кривая (ломаная) 
c.create_line([(105, 55), (155, 55), (130, 95)], smooth=1) # Кривая (сглаженная) 
#c.create_polygon([(205, 55), (255, 55), (230, 95)], fill="green")# Многоугольник зеленого цвета 

#c.create_rectangle((105, 105, 150, 130), fill="red", outline="grey", width="5") # Прямоугольник красного цвета с большой серой границей 
#c.create_text((10, 410), text="FACE SMILE", anchor="nw") # Текст 
c.create_oval((5, 205, 6, 206), outline="red") # Эта точка визуально обозначает угол привязки 

#c.create_text((105, 205), text="FACE SMILE", justify=LEFT, anchor="c") # Текст с заданным выравниванием 

#c.create_oval((105, 205, 106, 206), outline="red") 

## Еще один вариант 
#c.create_text((205, 205), text="Hello,\nmy friend!", justify=CENTER, anchor="se") 
#c.create_oval((205, 205, 206, 206), outline="red") 
#lbl=Label(f1,text="SMILE ROBOT",font="Calibri 20",fg="black", bg="pink")
var_smile=StringVar()
var_nose=StringVar()
var_eye1=StringVar()
var_eye2=StringVar()
var_head=StringVar()
btn_smile=Checkbutton(f1,text="smile",font="Calibri 16",bg="pink",variable=var_smile,onvalue=1, offvalue=0, height=4,width=10, command=add_smile)
btn_nose=Checkbutton(f1,text="nose",font="Calibri 16",bg="pink",variable=var_nose,onvalue=1, offvalue=0, height=4,width=10, command=add_nose)
btn_eye1=Checkbutton(f1,text="left eye",font="Calibri 16",bg="pink",variable=var_eye1,onvalue=1, offvalue=0, height=4,width=10)
btn_eye2=Checkbutton(f1,text="right eye",font="Calibri 16",bg="pink",variable=var_eye2,onvalue=1, offvalue=0, height=4,width=10)
btn_head=Checkbutton(f1,text="head",font="Calibri 26",fg="black",bg="green",relief=GROOVE,variable=var_head,offvalue="0",onvalue="1",command=add_head)

#lbl.pack(side=TOP)
btn_smile.pack()
btn_nose.pack()
btn_eye1.pack()
btn_eye2.pack()
btn_head.pack()
c.pack(side=LEFT) 

root.mainloop() 

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
