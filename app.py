
from tkinter import *

root=Tk()

s= StringVar()

result=0
first=0
second=0
res=""
fun=""
flag=0


def calculate(str):
    global first
    global second
    global res
    global fun
    global flag
    global result

    if flag==0:

        if str.isdigit():
            res=res+str
        else:
            fun=str
            first=int(res)
            res=""
            flag=1

    else:

        if str.isdigit():
            res=res+str
        elif str=="=":
            second=int(res)
            res=""
            if fun=="+":
                result=first + second
            elif fun=="-":
                result=first-second
            elif fun=="x":
                result=first*second
            elif fun=="/":
                result=first/second
            flag=0



    s.set("")


entry = Entry(root, textvariable=s)
entry.grid(row=0,columnspan=4)





nine= Button(root, text="9", command=calculate("9"))
nine.grid(row=1, column=0)
eight= Button(root, text="8", command=calculate("8"))
eight.grid(row=1, column=1)
seven= Button(root, text="7", command=calculate("7"))
seven.grid(row=1, column=2)
mul= Button(root, text="X", command=calculate("x"))
mul.grid(row=1, column=3)

four= Button(root, text="4", command=calculate("4"))
four.grid(row=2, column=0)
five= Button(root, text="5", command=calculate("5"))
five.grid(row=2, column=1)
six= Button(root, text="6", command=calculate("6"))
six.grid(row=2, column=2)
minus= Button(root, text="-", command=calculate("-"))
minus.grid(row=2, column=3)

one= Button(root, text="1", command=calculate("1"))
one.grid(row=3, column=0)
two= Button(root, text="2", command=calculate("2"))
two.grid(row=3, column=1)
three= Button(root, text="3", command=calculate("3"))
three.grid(row=3, column=2)
plus= Button(root, text="+", command=calculate("+"))
plus.grid(row=3, column=3)

div= Button(root, text="/", command=calculate("/"))
div.grid(row=4,column=0)
zero= Button(root, text="0", command=calculate("0"))
zero.grid(row=4, column=1)
dot= Button(root, text=".", command=calculate("."))
dot.grid(row=4, column=2)
equal= Button(root, text="=", command=calculate("="))
equal.grid(row=4, column=3)

root.mainloop()

