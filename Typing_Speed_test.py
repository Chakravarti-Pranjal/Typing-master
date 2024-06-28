from tkinter import *
import random 
from time import sleep
import threading

root = Tk()
root.resizable(0,0)
root.geometry('850x531')
root.title("Typing Test by Pranjal Chakravarti")
root.iconbitmap(r'C:\Users\dell\Desktop\mini project\logo.ico')


paragraph_list = ['''
         Python is a high-level, general-purpose programming language.
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
        . Many other paradigms are supported via extensions, 
          including design by contract and logic programming.
           
         
         ''']



word = random.shuffle(paragraph_list)      

################## Functionality part ############################

totaltime=30
time=0
wrongwords=0
elapsedtimeinminutes=0
def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,31):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/30
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    accuracy_percent_label.config(text=str(accuracy)+'%')


def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
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
    root.destroy()    

    ############ GUI part ############

bg=PhotoImage(file=r'C:\Users\dell\Desktop\mini project\bg.png' )

lab=Label(root,image=bg)
lab.pack()

welcome=Label( root,text="Welcome to typing test", font=('arial 10'),bg='#D2F59F')
welcome.place(x=632,y=13)

elapsed_time_label=Label(root,text=' Elapsed Time : ',font='algerian 15 bold' , bg='#D2F59F')
elapsed_time_label.place(x=590,y=50)

elapsed_timer_label=Label(root,text='0',font='algerian 15 bold' , bg='#D2F59F')
elapsed_timer_label.place(x=760,y=50)

remaining_time_label=Label(root,text='remainning Time : ',font='algerian 15 bold' , bg='#D2F59F')
remaining_time_label.place(x=590,y=80)

remaining_timer_label=Label(root,text='30',font='algerian 15 bold' , bg='#D2F59F')
remaining_timer_label.place(x=790,y=80)


wpm_labe=Label(root,text='wpm  : ',font='algerian 15 bold' , bg='#D2F59F')
wpm_labe.place(x=590,y=110)

wpm_count_label=Label(root,text='0',font='algerian 15 bold' , bg='#D2F59F')
wpm_count_label.place(x=665,y=110)


totalwords_label=Label(root,text='Total words : ',font='algerian 15 bold' , bg='#D2F59F')
totalwords_label.place(x=590,y=170)

totalwords_count_label=Label(root,text='0',font='algerian 15 bold' , bg='#D2F59F')
totalwords_count_label.place(x=750,y=170)

wrongwords_label=Label(root,text='wrong words : ',font='algerian 15 bold' , bg='#D2F59F')
wrongwords_label.place(x=590,y=200)

wrongwords_count_label=Label(root,text='0',font='algerian 15 bold' , bg='#D2F59F')
wrongwords_count_label.place(x=760,y=200)

accuracy_label=Label(root,text='accuracy : ',font='algerian 15 bold' , bg='#D2F59F')
accuracy_label.place(x=590,y=140)

accuracy_percent_label=Label(root,text='0',font='algerian 15 bold' , bg='#D2F59F')
accuracy_percent_label.place(x=720,y=140)

############ Buttons and Text ############

label_paragraph=Label(root,text=paragraph_list[0],font=('arial 13 bold'),bg='#f3fcda',fg='#535353',bd=0)
label_paragraph.place(x=10,y=10)

textarea=Text(root,height=18,width=62,font=('arial 13 bold'),fg='#535353',bd=0,padx=10,bg='#f3fcda')
textarea.place(x=2,y=240)

startButton=Button(root,height=2,width=18,activebackground='red',activeforeground='white',text='start',font='algerian 12 bold',bg='#D2F59F',bd=6,relief=GROOVE,command=start)
startButton.place(x=622,y=365)

resetButton=Button(root ,height=2,width=18,activebackground='red',activeforeground='white', text='Reset',font='algerian 12 bold',bg='#D2F59F',bd=6,relief=GROOVE,command=reset)
resetButton.place(x=622,y=423)

exitButton=Button(root ,height=2,width=18,activebackground='red',activeforeground='white', text='exit',bg='#D2F59F',font='algerian 12 bold',bd=6,relief=GROOVE,command=Exit)
exitButton.place(x=622,y=480)

root.mainloop()