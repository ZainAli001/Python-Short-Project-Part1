from cgitb import text
from tkinter import *
import speedtest

def speedCheck():
    check = speedtest.Speedtest()
    check.get_servers()
    down = str(round(check.download() / (10**6),3))+ "Mbps"
    up = str(round(check.upload() / (10**6),3))+ "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Test")
sp.iconbitmap("F:/Python/Project/20 Projects/InternetSpeed/logo.ico") 
sp.geometry("600x600")
sp.config(bg="#2193b0")


lab =Label(sp,text="Internet Speed Test",font=("Comic Sans MS",30,"bold"),bg="#2193b0",fg="white")
lab.place(x=40,y=60,height=60,width=500)


lab =Label(sp,text="Download Speed",font=("Time New Roman",15,"bold"))
lab.place(x=100,y=150,height=40,width=400)

lab_down =Label(sp,text="00",font=("Time New Roman",20,"bold"),relief='ridge', borderwidth=5)
lab_down.place(x=100,y=200,height=40,width=400)

lab =Label(sp,text="Upload Speed",font=("Time New Roman",15,"bold"))
lab.place(x=100,y=270,height=40,width=400)

lab_up =Label(sp,text="00",font=("Time New Roman",20,"bold"),relief='ridge', borderwidth=5 )
lab_up.place(x=100,y=320,height=40,width=400)

btn =Button(sp,text="Check Speed",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",bg="red",fg="white",command=speedCheck)
btn.place(x=200,y=390,height=40,width=200)

sp.mainloop()
