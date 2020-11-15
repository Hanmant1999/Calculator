from tkinter import *
root=Tk()
root.title("simple calculator")
e=Entry(root,width=40)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(number):
 current=e.get()
 e.delete(0,END)
 e.insert(0,str(current)+str(number))
 
def clear():
 e.delete(0,END) 
def add():
 number=e.get()
 global math
 math="addition"
 global num
 num=number
 e.delete(0,END)
 
def equal():
 snumber=e.get()
 e.delete(0,END)
 if math=="addition":
  e.insert(0,int(float((num)))+int(float((snumber))))
 elif math=="subtraction":
   e.insert(0,int(float(num))-int(float(snumber)))
 elif math=="multiplication":
   e.insert(0,int(float(num))*int(float(snumber)))
 elif math=="Division":
  e.insert(0,int(float(num))/int(float(snumber)))
 elif math=="power":
  e.insert(0,int(float(num))**int(float(snumber)))
def sub():
 number=e.get()
 global math
 math="subtraction"
 global num
 num=number
 e.delete(0,END)
def mul():
 number=e.get()
 global math
 math="multiplication"
 global num
 num=number
 e.delete(0,END)
def div():
 number=e.get()
 global math
 math="Division"
 global num
 num=number
 e.delete(0,END)
def power():
 number=e.get()
 global math
 math="power"
 global num
 num=number
 e.delete(0,END)
 

mybutton=Button(root,text=9,padx=25,pady=25,command=lambda:click(9))
mybutton1=Button(root,text=8,padx=25,pady=25,command=lambda:click(8))
mybutton2=Button(root,text=7,padx=25,pady=25,command=lambda:click(7))
mybutton3=Button(root,text=6,padx=25,pady=25,command=lambda:click(6))
mybutton4=Button(root,text=5,padx=25,pady=25,command=lambda:click(5))
mybutton5=Button(root,text=4,padx=25,pady=25,command=lambda:click(4))
mybutton6=Button(root,text=3,padx=25,pady=25,command=lambda:click(3))
mybutton7=Button(root,text=2,padx=25,pady=25,command=lambda:click(2))
mybutton8=Button(root,text=1,padx=25,pady=25,command=lambda:click(1))
mybutton9=Button(root,text="+",padx=25,pady=25,command=add)
mybutton10=Button(root,text=0,padx=25,pady=25,command=lambda:click(0))
mybutton11=Button(root,text="clear",padx=25,pady=25,command=clear)
mybutton12=Button(root,text="=",padx=25,pady=25,command=equal)
mybutton13=Button(root,text="-",padx=25,pady=25,command=sub)
mybutton14=Button(root,text="*",padx=25,pady=25,command=mul)
mybutton15=Button(root,text="/",padx=25,pady=25,command=div)
mybutton16=Button(root,text="^",padx=25,pady=25,command=power)
mybutton.grid(row=1,column=0)
mybutton1.grid(row=1,column=1)
mybutton2.grid(row=1,column=2)
mybutton3.grid(row=2,column=0)
mybutton4.grid(row=2,column=1)
mybutton5.grid(row=2,column=2)
mybutton6.grid(row=3,column=0)
mybutton7.grid(row=3,column=1)
mybutton8.grid(row=3,column=2)
mybutton9.grid(row=4,column=0)
mybutton10.grid(row=4,column=1)
mybutton11.grid(row=4,column=2)
mybutton12.grid(row=5,column=0)
mybutton13.grid(row=5,column=1)
mybutton14.grid(row=5,column=2)
mybutton15.grid(row=1,column=3)
mybutton16.grid(row=2,column=3)
root.mainloop()



