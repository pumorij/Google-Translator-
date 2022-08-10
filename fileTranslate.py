
from tkinter.filedialog import askopenfile
from tkinter import *
from translate import Translator
from googletrans import LANGUAGES
from distutils.command.install_egg_info import to_filename
import googletrans 

root=Tk()
root.state('zoomed')

bg=PhotoImage(file=r"C:\Users\dell6\Downloads\floral2.png")

label0=Label(root,image=bg)
label0.place(x=0,y=0)


def open_file():
    from tkinter.filedialog import askopenfile
    from translate import Translator
    translator=Translator(from_lang='en',to_lang=TranslateLanguageChoice.get())

    f=askopenfile(mode='r')
    contents=f.read()
    print(contents)
    result=translator.translate(contents)
    print(result)
    with open('C:\\Users\\dell6\\OneDrive\\Desktop\\dest.txt','w') as f:
        f.write(result)

label0=Label(root,text="Select File",font=("Helvetica",40,"bold"))
label0.place(x=650,y=100,height=60)

# button0 = Button(text="click here \n to select a file",font=(13),command=open_file)
# button0.place(x=700,y=200,height=50,width=160)


TranslateLanguageChoice = StringVar()


#tuple for choosing languages
LanguageChoices = LANGUAGES.values()
TranslateLanguageChoice.set('English')

#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(root,TranslateLanguageChoice,*LanguageChoices)

label1=Label(root,text="Select Translated Language",font=("Helvetica",20))
label1.place(x=270,y=250,height=40)

label2=NewLanguageChoiceMenu
label2.place(x=670,y=250,height=50,width=200)

button1 = Button(text="Click here \n to select file \n and to translate",font=(13),command=open_file,bg='light grey',fg='black',bd=3)
button1.place(x=650,y=400,height=100,width=260)

root.mainloop()























