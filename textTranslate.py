#importing modules
from cProfile import label
from cgitb import text
from re import L
from tkinter import *
from tkinter import font
from turtle import heading, width
from translate import Translator
from googletrans import LANGUAGES

# initializing window
Screen = Tk()
Screen.title("Language Translator with GUI")

Screen.state('zoomed')
bg=PhotoImage(file=r"C:\Users\dell6\Downloads\floral2.png")

label0=Label(Screen,image=bg)
label0.place(x=0,y=0)

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

#tuple for choosing languages
LanguageChoices = LANGUAGES.values()
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

label=Label(Screen,text="TRANSLATE YOUR TEXT",font=("Times",25,"bold"),bg="light grey")
label.place(x=600,y=50,height=50)

#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
label1=Label(Screen,text="Choose a Language",font=("Helvetica",25,"bold"),bg="light grey")
label1.place(x=400,y=120,height=50)

label2=InputLanguageChoiceMenu
label2.place(x=480,y=190,height=40,width=150)

#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
label3=Label(Screen,text="Translated Language",font=("Helvetica",25,"bold"),bg="light grey")
label3.place(x=800,y=120,height=50)

label4=NewLanguageChoiceMenu
label4.place(x=900,y=190,height=40,width=150)

label5=Label(Screen,text="Enter Text",font=("Helvetica",25),bg="light grey")
label5.place(x=480,y=260,height=50)
TextVar = StringVar()

TextBox = Entry(Screen,textvariable=TextVar,font=("Helvetica",25,"italic"))
TextBox.place(x=400,y=330,height=150,width=300)
TextBox.config(highlightbackground="black",highlightthickness=3)


label6=Label(Screen,text="Output Text",font=("Helvetica",25),bg="light grey")
label6.place(x=880,y=260,height=50)
OutputVar = StringVar()

TextBox = Entry(Screen,textvariable=OutputVar,font=("Helvetica",20,"italic"))
TextBox.place(x=800,y=330,height=150,width=300)
TextBox.config(highlightbackground="black",highlightthickness=3)

#Button for calling function

B = Button(Screen,text="Translate",command=Translate, relief = GROOVE,bg="grey",font=(10),fg='black',bd=3)
B.place(x=680,y=550,height=40,width=150)

mainloop()