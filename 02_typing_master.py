from tkinter import *
from tkinter import messagebox
from timeit import default_timer
import random 
import difflib

root = Tk()
root.resizable(0,0)
root.geometry('850x531')
root.title("Typing Test by Pranjal Chakravarti")
root.iconbitmap(r'C:\Users\dell\Desktop\mini project\logo.ico')


words = [''' Python is a high-level, general-purpose programming language.
        Its design  philosophy emphasizes code readability with the use of
        significant indentation.''',

         '''Python uses dynamic typing and a combination of reference 
         counting and a cycle-detecting garbage collector for memory 
         management. It uses dynamic name resolution (late binding), 
         which binds method and variable names during program execution.''',
         
         '''Python is dynamically-typed and garbage-collected. It supports
          multiple programming paradigms, including structured, 
          object-oriented and functional programming. It is often 
          described as a "batteries included" language due to its
           comprehensive standard library.''',
         
         '''Guido van Rossum began working on Python in the late 1980s
          as a successor to the ABC programming language and first 
          released it in 1991 as Python 0.9.0. Python 2.0 was released
           in 2000 and introduced new features such as list 
           comprehensions, cycle-detecting garbage collection, 
           reference counting, and Unicode support. Python 3.0, 
           released in 2008, was a major revision that is not 
           completely backward-compatible with earlier versions. ''',
         
         '''Python is a multi-paradigm programming language. 
         Object-oriented programming and structured programming 
         are fully supported, and many of its features support 
         functional programming and aspect-oriented programming
          (including metaprogramming and metaobjects). Many other 
          paradigms are supported via extensions, including design
           by contract and logic programming.
         
         ''']



word = random.choice(words)      

################## Function part ############################

def Result():
    global word
    global text_
    global start

    string=f'{text_.get(1.0,END)}'
    print(string)

    end=default_timer()

    time=round(end-start,2)
    print(time)

    speed=round(len(word.split())*60/time,2)
    print(speed)

    accuracy=difflib.SequenceMatcher(None,word,string).ratio()
    accuracy=str(round(accuracy*100,2))
    print(accuracy)

    message=('Time= '+str(time)+'second',
    '\nAccuracy= '+str(accuracy)+'%',
    '\nSpeed= '+str(speed)+'wpm')

    messagebox.showinfo('Result',(message))


def started():
    word = random.choice(words) 
    content.config(text=word)
    
def Reset():
  pass    

def Exit():
    root.destroy()    

    ############ GUI part ############

bg=PhotoImage(file=r'C:\Users\dell\Desktop\mini project\bg.png' )

lab=Label(root,image=bg)
lab.pack()

welcome=Label( root,text="Welcome to Pranjal's typing test", font=('arial 10'),bg='#D2F59F')
welcome.place(x=632,y=13)

time=Label(root,text=' total Time : ',font='algerian 15 bold' , bg='#D2F59F')
time.place(x=590,y=50)

remaining_time=Label(root,text='remainning Time : ',font='algerian 15 bold' , bg='#D2F59F')
remaining_time.place(x=590,y=80)

speed=Label(root,text='speed : ',font='algerian 15 bold' , bg='#D2F59F')
speed.place(x=590,y=110)

accuracy=Label(root,text='accuracy : ',font='algerian 15 bold' , bg='#D2F59F')
accuracy.place(x=590,y=140)

total_word=Label(root,text='Total word : ',font='algerian 15 bold' , bg='#D2F59F')
total_word.place(x=590,y=170)

wrong_word=Label(root,text='wrong word: ',font='algerian 15 bold' , bg='#D2F59F')
wrong_word.place(x=590,y=200)

# content=Label(root,font=('arial 13 bold'),bg='#f3fcda',fg='#535353',bd=0)
# content.place(x=10,y=10)

text_=Text(root,height=18,width=62,font=('arial 13 bold'),fg='#535353',bd=0,padx=10,bg='#f3fcda')
text_.place(x=2,y=240)

start=Button(root,height=2,width=29,text='start',bg='#D2F59F',bd=6,relief=GROOVE,command=started)
start.place(x=627,y=300)

reset=Button(root ,height=2,width=29, text='reset',bg='#D2F59F',bd=4,relief=GROOVE,command=Reset)
reset.place(x=629,y=365)


result=Button(root ,height=2,width=29, text='result',bg='#D2F59F',bd=4,relief=GROOVE,command=Result)
result.place(x=629,y=424)

exit=Button(root ,height=2,width=29, text='exit',bg='#D2F59F',bd=4,relief=GROOVE,command=Exit)
exit.place(x=630,y=487)

start=default_timer()

root.mainloop()