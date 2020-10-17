from tkinter  import *
from tkinter  import messagebox
import random 
f = Tk()
f.title('Russian Roulette')
f.minsize(400,400)
f.maxsize(400,400)
f.configure(bg='purple')
lbl = Label(f,text='Welcome to Russian Roulette',font=("Arial Bold", 15),bg="pink",width=30,height=1)
lbl.place(x=20,y=30)
lbl = Label(f,text='please choose your bullet',font=("Arial Bold", 10),bg="pink",width=30,height=2)
lbl.place(x=85,y=70)
i1 = PhotoImage(file="a.png")
i2 = PhotoImage(file="c.png")

#Random Number#
n = list(range(1,6))
numberrandom = random.sample(n,k=1)
nn1 = int(numberrandom[0])

m = 0

#Function#
def change():
    global m
    if nn1 == 1 :
     b1["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b1["image"] = i2
     m = m+1        
b1 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b1.place(x=50,y=200)

def change():
    global m
    if nn1 == 2 :
     b2["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b2["image"] = i2
     m = m+1        
b2 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b2.place(x=175,y=200)

def change():
    global m
    if nn1 == 3 :
     b3["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b3["image"] = i2
     m = m+1        
b3 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b3.place(x=300,y=200)

def change():
    global m
    if nn1 == 4 :
     b4["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b4["image"] = i2
     m = m+1        
b4 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b4.place(x=50,y=300)

def change():
    global m
    if nn1 == 5 :
     b5["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b5["image"] = i2
     m = m+1        
b5 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b5.place(x=175,y=300)

def change():
    global m
    if nn1 == 6 :
     b6["image"] = i1
     messagebox.showinfo("Bang!!", "You die")
     restart()
    else:       
     b6["image"] = i2
     m = m+1
b6 = Button(f,image=i1,text='OK',command=change,bg='black',width=50,height=50)
b6.place(x=300,y=300)

def restart():
    b1["image"] = i1
    b2["image"] = i1
    b3["image"] = i1
    b4["image"] = i1
    b5["image"] = i1
    b6["image"] = i1
    n = list(range(1,6))
    numberrandom = random.sample(n,k=1)
    global nn1
    nn1 = int(numberrandom[0])
    print(nn1)
    
f.mainloop()



