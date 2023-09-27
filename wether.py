import requests
import json
import tkinter as t

apikey="20fe45e385ee4f804d3edb0d208d29db"
base="https://api.openweathermap.org/data/2.5/weather?q="
root=t.Tk()
root.title("WETHER FORECAST")
root.geometry("900x300")
root.configure(bg="lightgray")
l=t.Label(root,text="WELCOME TO WETHER REPORT PAGE",font=("times new roman",30))
l.configure(bg="lightgray",fg="blue")
l.place(x="450",y="50")
l1=t.Label(root,text=" ENTER CITY NAME FOR REPORT :",font=("times new roman",20))
l1.configure(bg="lightgray")
l1.place(x="220",y="150")
e=t.Entry(root)
e.place(x="670",y="160")


def get_name():
    nam=e.get()
    url=base+nam+"&appid="+apikey
    res=requests.get(url)
    dat=res.json()
    print(dat)
    
    l2=t.Label(root,text="Temperature : "+str(dat["main"]["temp"]),font=("airal",20))
    l2.configure(fg="green",bg="lightgray")
    l2.place(x="700",y="270")
    
    l3=t.Label(root,text="Humidity : "+str(dat["main"]["humidity"]),font=("airal",20))
    l3.configure(fg="green",bg="lightgray")
    l3.place(x="700",y="330")
    
    l4=t.Label(root,text="Wind Speed : "+str(dat["wind"]["speed"]),font=("airal",20))
    l4.configure(fg="green",bg="lightgray")
    l4.place(x="700",y="390")
    
    l5=t.Label(root,text="Description : "+str(dat["weather"][0]["description"]),font=("airal",20))
    l5.configure(fg="green",bg="lightgray")
    l5.place(x="700",y="450")
   
    
    
    
b=t.Button(root,text="GET REPORT",command=get_name)
b.place(x="700",y="220")  
    

root.mainloop()