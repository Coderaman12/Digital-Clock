from tkinter import *
import time


clk= Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")
clk.config(bg="#0C1E28")



def clock():
   hr = str(time.strftime("%H"))
   min = str(time.strftime("%M"))
   sec = str(time.strftime("%S"))
   print(hr,min,sec)
   if int(hr) > 12 and int(min) > 0 :
      lb_dn.config(text="PM")

   if int(hr) > 12 :
      hr = str(int(int(hr)-12))
      
      
   lb_hr.config(text=hr)
   lb_min.config(text=min)
   lb_sec.config(text=sec)
   
   lb_hr.after(200,clock)     # to make clock updated every second
      



lb_hr = Label(clk,text="12",font=("Times 20 bold",75,"bold"),bg="#087587",fg="white")
lb_hr.place(x=350,y=200,width=150,height=150)

lb_hr_txt = Label(clk,text="HOUR",font=("Times 20 bold",20,"bold"),bg = "#087587",fg = "white")
lb_hr_txt.place(x=350,y=360,width=150,height=50)


lb_min = Label(clk,text="60",font=("Times 20 bold",75,"bold"),bg="#008EA4",fg="white")
lb_min.place(x=520,y=200,width=150,height=150)

lb_min_txt = Label(clk,text="MINUTE",font=("Times 20 bold",20,"bold"),bg = "#008EA4",fg = "white")
lb_min_txt.place(x=520,y=360,width=150,height=50)



lb_sec = Label(clk,text="60",font=("Times 20 bold",75,"bold"),bg="#06B4B8",fg="white")
lb_sec.place(x=690,y=200,width=150,height=150)

lb_sec_txt = Label(clk,text="SECOND",font=("Times 20 bold",20,"bold"),bg = "#06B4B8",fg = "white")
lb_sec_txt.place(x=690,y=360,width=150,height=50)



lb_dn = Label(clk,text="AM",font=("Times 20 bold",75,"bold"),bg="#9F0646",fg="white")
lb_dn.place(x=860,y=200,width=150,height=150)

lb_dn_txt = Label(clk,text="NOON",font=("Times 20 bold",20,"bold"),bg = "#9F0646",fg = "white")
lb_dn_txt.place(x=860,y=360,width=150,height=50)


clock()
clk.mainloop()