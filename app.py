
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
            res=result
        else:
            second = int(res)
            res = ""
            if fun == "+":
                result = first + second
            elif fun == "-":
                result = first - second
            elif fun == "x":
                result = first * second
            elif fun == "/":
                result = first / second

            first=result





    s.set(res)

def clear():
    s.set("")
    global result
    global first
    global second
    global res
    global fun
    global flag
    result = 0
    first = 0
    second = 0
    res = ""
    fun = ""
    flag = 0


entry = Entry(root, textvariable=s)
entry.grid(row=0,columnspan=4)





nine= Button(root, text="9", command= lambda: calculate("9"),width=5)
nine.grid(row=1, column=0)
eight= Button(root, text="8", command= lambda: calculate("8"),width=5)
eight.grid(row=1, column=1)
seven= Button(root, text="7", command= lambda: calculate("7"),width=5)
seven.grid(row=1, column=2)
mul= Button(root, text="X", command= lambda: calculate("x"),width=5)
mul.grid(row=1, column=3)

four= Button(root, text="4", command= lambda: calculate("4"),width=5)
four.grid(row=2, column=0)
five= Button(root, text="5", command= lambda: calculate("5"),width=5)
five.grid(row=2, column=1)
six= Button(root, text="6", command= lambda: calculate("6"),width=5)
six.grid(row=2, column=2)
minus= Button(root, text="-", command= lambda: calculate("-"),width=5)
minus.grid(row=2, column=3)

one= Button(root, text="1", command= lambda: calculate("1"),width=5)
one.grid(row=3, column=0)
two= Button(root, text="2", command= lambda: calculate("2"),width=5)
two.grid(row=3, column=1)
three= Button(root, text="3", command= lambda: calculate("3"),width=5)
three.grid(row=3, column=2)
plus= Button(root, text="+", command= lambda: calculate("+"),width=5)
plus.grid(row=3, column=3)

div= Button(root, text="/", command= lambda: calculate("/"),width=5)
div.grid(row=4,column=0)
zero= Button(root, text="0", command= lambda: calculate("0"),width=5)
zero.grid(row=4, column=1)
clear= Button(root, text="clear", command= clear,width=5)
clear.grid(row=4, column=2)
equal= Button(root, text="=", command= lambda: calculate("="),width=5)
equal.grid(row=4, column=3)

root.mainloop()


