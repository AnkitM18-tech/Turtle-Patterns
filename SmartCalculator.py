from tkinter import *

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a ==0 and l%b ==0:
            return l
        l+=1

def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1


def extract_from_text(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text=textin.get()
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                l1st.delete(0,END)
                l1st.insert(END,r)
            except:
                l1st.delete(0,END)
                l1st.insert(END,"Something Went Wrong!! Please Enter again")
            finally:
                break
        elif word.upper() not in operations.keys():
            l1st.delete(0,END)
            l1st.insert(END,"Something Went Wrong!! Please Enter again")


operations={"ADD":add,"ADDITION":add,"SUM":add,"PLUS":add,
            "SUBTRACT":subtract,"MINUS":subtract,"DIFFERENCE":subtract,
            "LCM":lcm,"HCF":hcf,"PRODUCT":multiply,"MULTIPLY":multiply,"INTO":multiply,
            "MULTIPLICATION":multiply,"DIVISION":divide,"DIVIDE":divide,"BY":divide,"MOD":mod,"REMAINDER":mod,
            "MODULUS":mod}



win=Tk()
win.geometry("500x400")
win.title("Python")
win.configure(bg="lightskyblue")

l1=Label(win,text="I am a smart Calculator",width=20,padx=3)
l1.place(x=150,y=10)

l2=Label(win,text="My Name is Python",padx=3)
l2.place(x=170,y=40)

l3=Label(win,text="How can I help you?",padx=3)
l3.place(x=168,y=130)

textin=StringVar()
e1=Entry(win,width=40,textvariable=textin)
e1.place(x=110,y=160)

b1=Button(win,text="Just This!",padx=3,command=calculate)
b1.place(x=200,y=200)

l1st=Listbox(win,width=40,height=4)
l1st.place(x=110,y=230)

win.mainloop()