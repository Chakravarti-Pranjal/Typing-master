from tkinter import *
from tkinter import messagebox
import random 
from time import sleep
import threading

root=Tk()
root.title('Login')
root.geometry('1160x650+300+200')
root.configure(bg='#fff')
root.resizable(0,0)

def signin():
    username=user.get()
    password=code.get()

    ######################## _____------------------------------------

    if username=='Pranjal' and password== '12345':
        screen = Toplevel(root)
        
        screen.geometry('850x531')
        screen.title("Typing Test by Pranjal Chakravarti")
        screen.iconbitmap(r'C:\Users\dell\Desktop\mini project\logo.ico')
        screen.resizable(0,0)


        paragraph_list = ['''

         Python is a high-level, general-purpose programming language.
        Its design  philosophy emphasizes code readability with the use 
        of significant indentation.''',

        '''Python uses dynamic typing and a combination of reference 
          counting and a cycle-detecting garbage collector for memory 
          management. It uses dynamic name resolution (late binding), 
          which binds method and variable names during program execution.''',
         
         '''Python is dynamically-typed and garbage-collected. It 
        supports multiple programming paradigms, including structured, 
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

        word=random.shuffle(paragraph_list)

        totaltime=60
        time=0
        
        def start_timer():
            wrongwords=0
            elapsedtimeinminutes=0
            startButton.config(state=DISABLED)
            global time
            textarea.config(state=NORMAL)
            textarea.focus()

            for time in range(1,61):
                elapsed_timer_label.config(text=time)
                remainingtime=totaltime-time
                remaining_timer_label.config(text=remainingtime)
                sleep(1)
                screen.update()

            textarea.config(state=DISABLED)
            resetButton.config(state=NORMAL)

        def count():
            global wrongwords
            while time!=totaltime:
                entered_paragraph=textarea.get(1.0,END).split()
                totalwords=len(entered_paragraph)

            totalwords_count_label.config(text=totalwords)
            para_word_list=label_paragraph['text'].split()

            for pair in list (zip(para_word_list,entered_paragraph)):
                if pair[0]!=pair[1]:
                         wrongwords+=1

            wrongwords_count_label.config(text=wrongwords)

            elapsedtimeinminutes=time/60
            wpm=(totalwords-wrongwords)/elapsedtimeinminutes
            wpm_count_label.config(text=wpm)
            gross_wpm=totalwords/elapsedtimeinminutes
            accuracy=wpm/gross_wpm*100
            accuracy=round(accuracy)  
            accuracy_percent_label.config(text=str(accuracy)+'%')

        def start():
            t1=threading.Thread(target=start_timer)
            t1.start()
            t2=threading.Thread(target=count)
            t2.start()

        def reset():
            global time,elapsedtimeinminutes
            time=0
            elapsedtimeinminutes=0
            startButton.config(state=NORMAL)                         
            resetButton.config(state=DISABLED)
            textarea.config(state=NORMAL)
            textarea.delete(1.0,END)
            textarea.config(state=DISABLED)

            elapsed_timer_label.config(text='0')
            remaining_timer_label.config(text='0')
            wpm_count_label.config(text='0')
            accuracy_percent_label.config(text='0')
            totalwords_count_label.config(text='0')
            wrongwords_count_label.config(text='0')

        def Exit():
            screen.destroy()

        bg=PhotoImage(file=r'C:\Users\dell\Desktop\mini project\bg.png' )  
        lab=Label(screen,image=bg)
        lab.pack()  

        welcome=Label( screen,text="Welcome to Pranjal's typing test", font=('arial 10'),bg='#D2F59F')
        welcome.place(x=632,y=13)  

        elapsed_time_label=Label(screen,text=' Elapsed Time : ',font='algerian 15 bold' , bg='#D2F59F')
        elapsed_time_label.place(x=590,y=50)

        elapsed_timer_label=Label(screen,text='0',font='algerian 15 bold' , bg='#D2F59F')
        elapsed_timer_label.place(x=760,y=50)

        remaining_time_label=Label(screen,text='remainning Time : ',font='algerian 15 bold' , bg='#D2F59F')
        remaining_time_label.place(x=590,y=80)

        remaining_timer_label=Label(screen,text='60',font='algerian 15 bold' , bg='#D2F59F')
        remaining_timer_label.place(x=790,y=80)

        wpm_labe=Label(screen,text='wpm  : ',font='algerian 15 bold' , bg='#D2F59F')
        wpm_labe.place(x=590,y=110)

        wpm_count_label=Label(screen,text='0',font='algerian 15 bold' , bg='#D2F59F')
        wpm_count_label.place(x=665,y=110)

        totalwords_label=Label(screen,text='Total words : ',font='algerian 15 bold' , bg='#D2F59F')
        totalwords_label.place(x=590,y=170)

        totalwords_count_label=Label(screen,text='0',font='algerian 15 bold' , bg='#D2F59F')
        totalwords_count_label.place(x=750,y=170)

        wrongwords_label=Label(screen,text='wrong words : ',font='algerian 15 bold' , bg='#D2F59F')
        wrongwords_label.place(x=590,y=200)

        wrongwords_count_label=Label(screen,text='0',font='algerian 15 bold' , bg='#D2F59F')
        wrongwords_count_label.place(x=760,y=200)

        accuracy_label=Label(screen,text='accuracy : ',font='algerian 15 bold' , bg='#D2F59F')
        accuracy_label.place(x=590,y=140)

        accuracy_percent_label=Label(screen,text='0',font='algerian 15 bold' , bg='#D2F59F')
        accuracy_percent_label.place(x=720,y=140)

        label_paragraph=Label(screen,text=paragraph_list[0],font=('arial 13 bold'),bg='#f3fcda',fg='#535353',bd=0)
        label_paragraph.place(x=10,y=10)

        textarea=Text(screen,height=18,width=62,font=('arial 13 bold'),fg='#535353',bd=0,padx=10,bg='#f3fcda')
        textarea.place(x=2,y=240)

        startButton=Button(screen,height=2,width=18,activebackground='red',activeforeground='white',text='start',font='algerian 12 bold',bg='#D2F59F',bd=6,relief=GROOVE,command=start)
        startButton.place(x=622,y=365)

        resetButton=Button(screen ,height=2,width=18,activebackground='red',activeforeground='white', text='Reset',font='algerian 12 bold',bg='#D2F59F',bd=6,relief=GROOVE,command=reset)
        resetButton.place(x=622,y=423)

        exitButton=Button(screen ,height=2,width=18,activebackground='red',activeforeground='white', text='exit',bg='#D2F59F',font='algerian 12 bold',bd=6,relief=GROOVE,command=Exit)
        exitButton.place(x=622,y=480)

        screen.mainloop()

#################### ----------------------
    elif username!='Pranjal' and password!='12345':
        messagebox.showerror('Invalid','Invalid username and password')

    elif password!='12345': 
        messagebox.showerror('Invalid','Invalid  password!   ')  

    elif username!='Pranjal':
        messagebox.showerror('Invalid','Invalid username!')      

        


####### ---------------------------

img=PhotoImage(file=r'C:\Users\dell\Pictures\login2.png')
Label(root,image=img,bg='white').place(x=-90,y=0)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=780,y=150)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=100,y=5)

########### -------------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',bd=0,bg='white',font=('Microsoft YaHei UI Light',18))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=115)

############----------------------------------

def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',bd=0,bg='white',font=('Microsoft YaHei UI Light',18))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=185)

############################# Button ------------

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',bd=0,command=signin).place(x=35,y=230)

label=Label(frame,text="Don't have an account?",fg='black',bg=
'white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=280)

sign_up=Button(frame,width=6,text='sign up',bd=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=212,y=280)

root.mainloop()