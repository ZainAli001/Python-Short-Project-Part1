from tkinter import *
import main


st = Tk()
st.title("Shutdown App")
st.iconbitmap("F:/Python/Project/20 Projects/shutDownApp/icon.ico") 
st.geometry("550x500")
st.config(bg="#2193b0")


restartButton =Button(st,text="Restart",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=main.restart)
restartButton.place(x=200,y=60,height=40,width=150)

restartTimeButton =Button(st,text="Restart Time",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=main.restartTime)
restartTimeButton.place(x=200,y=160,height=40,width=150)

logOutButton =Button(st,text="Log Out",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=main.logout)
logOutButton.place(x=200,y=260,height=40,width=150)

shutDownButton =Button(st,text="Shutdown",font=("Time New Roman",10,"bold"),relief=RAISED,cursor="plus",command=main.shutdown)
shutDownButton.place(x=200,y=360,height=40,width=150)


st.mainloop()