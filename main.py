from cProfile import label
from tkinter import *;
from PIL import ImageTk , Image
from subprocess import call

root = Tk()
root.title("Language Translator")

root.state('zoomed')
root.configure(bg='pink')

def openTextTranslate():
    call(["python","textTranslate.py"])

def openFileTranslate():
    call(["python","fileTranslate.py"])    

# image 
img=ImageTk.PhotoImage(Image.open("mainImage.png"))
labelImg=Label(root,image=img,height=250,width=450)
labelImg.pack(pady=10)

label0=Label(root,text="You can translate text or a file !!",font=("Times",40,"bold"),bg="pink")
label0.place(x=420,y=300,height=70)


label1=Label(root,text="Translate text",font=("Helvetica",30),bg="pink")
label1.place(x=420,y=400,height=70)

label2=Label(root,text="Translate a File",font=("Helvetica",30),bg="pink")
label2.place(x=820,y=400,height=70)

# border = LabelFrame(root,bd=3,bg="black")
# border.pack()

button1 = Button(text="click here \n to translate text",font=(13),command=openTextTranslate,bd=3,bg='light grey',fg='black')
button1.place(x=450,y=500,height=50,width=160)
# button1.pack(padx=450,pady=500)
# button1.config(highlightbackground="black",highlightthickness=3,highlightcolor="black")


button2 = Button(text="click here \n to translate a file",font=(13),command=openFileTranslate,bd=3,bg='light grey',fg='black')
button2.place(x=854,y=500,height=50,width=160)



mainloop()