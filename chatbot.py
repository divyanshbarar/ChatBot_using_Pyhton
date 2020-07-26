from tkinter import *
import pyjokes
import time
import wikipedia
root=Tk()
root.configure(bg="red")
#def hasNumbers(inputString):
 #   return any(char.isdigit() for char in inputString)
def send(event=None):
    send="YOU => " + e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello" or e.get()=="hi" or e.get()=="hey" or e.get()=="hi rocky"):
        txt.insert(END,"\n"+"ROCKY = >  Hi friend!!!")
    elif(e.get()=="how are you" or e.get()=="what about you" or e.get()=="what are you doing"):
        txt.insert(END,"\n"+"ROCKY = >  ROCKY is good. What about you ??? ")
    elif(e.get()=="fine" or e.get()=="good" or e.get()=="same here" or e.get()=="nice" or e.get()=="very good" or e.get()=="fantastic"):
        txt.insert(END,"\n"+"ROCKY = > nice to hear you  ")     
    elif(e.get()=="what can you do for me"):
        txt.insert(END,"\n"+"ROCKY = >  ROCKY can tell you a joke... ")
    elif(e.get()=="tell me a joke"):
        txt.insert(END,"\n"+"ROCKY = >" + pyjokes.get_joke())    
    elif(e.get()=="tell me the time" or e.get()=="tell me the date" or e.get()=="what time it is" or e.get()=="time"):
        txt.insert(END,"\n"+"ROCKY = >" + time.asctime())  
    elif(e.get()=="bye"):
        root.destroy()
    elif(len(e.get())==0):
        txt.insert(END,"\n"+"ROCKY = >Type Something before hitting ENTER ")
    else:
        try:
           txt.insert(END,"\n"+"ROCKY = >" + wikipedia.summary(e.get(),sentences=2))     
        except Exception as PageError:
           txt.insert(END,"\n"+"ROCKY = >  I can't understand... though ROCKY is genius ")
    e.delete(0,END)
txt=Text(root)
txt.configure(bg="yellow")
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=60)
e1=Entry(root,width=60)
e1.grid(row=2,column=0)
e1.insert(0,"type here :with proper spacing in lowercase only")
e1.configure(bg="yellow",state=DISABLED)
e.grid(row=1,column=0)
root.bind('<Return>', send)
send=Button(root,text="SEND",command=send).grid(row=1,column=1)

root.title("ROCKY CHATBOT")
root.mainloop()