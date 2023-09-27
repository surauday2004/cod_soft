import tkinter as t
import string
import random

root = t.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg="skyblue")

def get_input():
    size=int(e1.get())
    nam=e.get()
    char=string.printable
    pas=''.join(random.choice(char) for _ in range(size))
    c.create_text(80,200,text="Hello "+nam+" your password:\n")
    c.create_text(300,200,text=pas,fill="red",font=("Arial",20))

c=t.Canvas(root,height="300",width="500")
c.create_text(250,10,text="PASSWORD GENERATOR")
c.create_text(50,50,text="Enter Name:")
e=t.Entry(root)
c.create_text(50,80,text="Password Length:")
e1=t.Entry(root)
e1.place(x="350",y="120")
e.place(x="340",y="90")
c.place(x="250",y="50")
b=t.Button(root,text="CREATE",command=get_input)
b.place(x="400",y="150")


   
    
    


root.mainloop()
