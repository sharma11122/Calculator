from tkinter import*

top=Tk()
top.title("Calcutor")
top.geometry("365x490")

def click(number):
    global operator
    operator+=str(number)
    text.set(operator)

def clear():
    global operator
    operator=''
    text.set(operator)

def equal():
    global operator
    result=eval(operator)
    operator=str(result)
    text.set(result)
############################################################
def on_enter7(e):
    btn7.configure(bg='red')
def on_leave7(e):
    btn7.configure(bg='violet')

def on_enter8(e):
    btn8.configure(bg='red')
def on_leave8(e):
    btn8.configure(bg='violet')

def on_enter9(e):
    btn9.configure(bg='red')
def on_leave9(e):
    btn9.configure(bg='violet')

def on_enter6(e):
    btn6.configure(bg='red')
def on_leave6(e):
    btn6.configure(bg='violet')

def on_enter5(e):
    btn5.configure(bg='red')
def on_leave5(e):
    btn5.configure(bg='violet')


def on_enter4(e):
    btn4.configure(bg='red')
def on_leave4(e):
    btn4.configure(bg='violet')


def on_enter3(e):
    btn3.configure(bg='red')
def on_leave3(e):
    btn3.configure(bg='violet')


def on_enter2(e):
    btn2.configure(bg='red')
def on_leave2(e):
    btn2.configure(bg='violet')

def on_enter1(e):
    btn1.configure(bg='red')
def on_leave1(e):
    btn1.configure(bg='violet')

def on_enter0(e):
    btn0.configure(bg='red')
def on_leave0(e):
    btn0.configure(bg='violet')

def on_enterdiv(e):
    btndiv.configure(bg='red')
def on_leavediv(e):
    btndiv.configure(bg='violet')

def on_entermul(e):
    btnmul.configure(bg='red')
def on_leavemul(e):
    btnmul.configure(bg='violet')

def on_enteradd(e):
    btnadd.configure(bg='red')
def on_leaveadd(e):
    btnadd.configure(bg='violet')

def on_entersub(e):
    btnsub.configure(bg='red')
def on_leavesub(e):
    btnsub.configure(bg='violet')

def on_enterclear(e):
    btnclear.configure(bg='red')
def on_leaveclear(e):
    btnclear.configure(bg='violet')

def on_enterequal(e):
    btnequal.configure(bg='red')
def on_leaveequal(e):
    btnequal.configure(bg='violet')


text=StringVar()
operator=''

entry1=Entry(top,bg="light green",font=('arial',20,'italic bold'),bd='30',justify="right",textvariable=text)
entry1.grid(row=0,columnspan=4)

btn7=Button(top,text="7",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(7),activebackground="green",activeforeground="violet")
btn7.grid(row=1,column=0)

btn8=Button(top,text="8",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(8),activebackground="green",activeforeground="white")
btn8.grid(row=1,column=1)

btn9=Button(top,text="9",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(9),activebackground="green",activeforeground="white")
btn9.grid(row=1,column=2)

btnadd=Button(top,text="+",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click('+'),activebackground="green",activeforeground="white")
btnadd.grid(row=1,column=3)

btn4=Button(top,text="4",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(4),activebackground="green",activeforeground="white")
btn4.grid(row=2,column=0)

btn5=Button(top,text="5",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(5),activebackground="green",activeforeground="white")
btn5.grid(row=2,column=1)

btn6=Button(top,text="6",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(6),activebackground="green",activeforeground="white")
btn6.grid(row=2,column=2)

btnsub=Button(top,text="-",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click('-'),activebackground="green",activeforeground="white")
btnsub.grid(row=2,column=3)


btn3=Button(top,text="3",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(3),activebackground="green",activeforeground="white")
btn3.grid(row=3,column=0)

btn2=Button(top,text="2",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(2),activebackground="green",activeforeground="white")
btn2.grid(row=3,column=1)

btn1=Button(top,text="1",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(1),activebackground="green",activeforeground="white")
btn1.grid(row=3,column=2)

btnmul=Button(top,text="X",font=('arial',20,'italic bold'),bd='8',padx='16',pady='18',command=lambda:click('*'),activebackground="green",activeforeground="white")
btnmul.grid(row=3,column=3)


btn0=Button(top,text="0",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click(0),activebackground="green",activeforeground="white")
btn0.grid(row=4,column=0)

btnclear=Button(top,text="C",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=clear,activebackground="green",activeforeground="white")
btnclear.grid(row=4,column=1)

btnequal=Button(top,text="=",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=equal,activebackground="green",activeforeground="white")
btnequal.grid(row=4,column=2)

btndiv=Button(top,text="/",font=('arial',20,'italic bold'),bd='8',padx='18',pady='18',command=lambda:click('/'),activebackground="green",activeforeground="white")
btndiv.grid(row=4,column=3)

#############################################################

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)


btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)


btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)


btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)


btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)


btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)


btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)


btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)



top.mainloop()