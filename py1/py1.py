from tkinter import *
foto_list=["pc1.png","pc2.png","pc3.png","pc4.png"]
def list_to_txt(event):
    global can,foto#----------------
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)#---------------
    foto=PhotoImage(file=foto_list[valik[0]])#-------------
    can.create_image(0,0,image=foto,anchor=NW)#-----------------
def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)

def opisanie(txt_to_list,list_to_txt):
    text = txt.get(0.0, END)
    print(list(text))
    if text=="pc1.png\n":
        ttt="i3 10100"
    elif text=="pc2.png\n":
        ttt="i5 10400"
    elif text=="pc3.png\n":
        ttt="i7 10700f "
    elif text=="pc4.png\n":
        ttt=" i9 10900kf"
    opis.config(text=ttt)

win=Tk()
lbox=Listbox(win,width=70,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)

bt=Button(text='Info', command=opisanie).pack()#, command=op
opis=Label(win, text="DESCRIPTION", width=20, height=20)
opis.pack(row=1,column=2)   
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=10,width=20,wrap=WORD)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=200,bg="gold")#--------------
can.grid(row=1,column=0,columnspan=2)#--------------------
foto=PhotoImage(file="pc2.png")#----------------
can.create_image(0,0,image=foto,anchor=NW)#-----------------
win.mainloop()
opis.pack()
