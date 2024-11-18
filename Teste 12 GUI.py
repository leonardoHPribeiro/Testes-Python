import tkinter
import tkinter.simpledialog
from tkinter import *
from time import sleep

def click():
    temp.config(text= tb1)

    tb.config()
window = Tk()
window.geometry('800x600')
window.title('papagaio do clima')

gordão = PhotoImage(file= 'img.png')
icon = PhotoImage(file= 'sol.png')
window.iconphoto(True,icon)
window.config(background= 'gray')
label = Label(window,
              text= 'detalhes do clima em sua cidade',
              font=('arial', 10,'bold'),
              fg= 'white',
              bg='black',
              relief=RAISED,
              bd= '5',
              padx= '5',
              pady= '5',
              image= gordão,
              compound= 'bottom')
label.pack()
#uma alternativa para fazer o display do texto é usar o código
#label.place(x=0,y=0) #

label1 = Label(window,
              text= 'A besta observa',
              font=('arial',10,'bold'),
              fg= 'white',
              bg= 'black',
              relief=RAISED,
              bd= '5',
              padx= '94',
              pady= '5')
label1.place(x=250,y=235)

#ask = tkinter.simpledialog.Dialog(window)

tb = tkinter.Text(window,height= 1,width= 55)
#tb.config(command=)
tb.config(font=('arial', 10,'bold'),
          bg= 'white',
          fg= 'black',
          relief=RAISED,
          bd= '5',
          padx= '5',
          pady= '5')
tb.place(x=195, y=280)

tb1= print(tb)

button = Button(window, text= 'clique aqui e o papagaio dira os detalhes do clima de sua cidade')
button.config(command= click)
button.config(font=('arial', 10,'bold'),
              bg= 'black',
              fg= 'white',
              activebackground= 'yellow',
              activeforeground= 'green',
                relief=RAISED,
                bd= '5',
                padx= '5',
                pady= '5')
papa= PhotoImage(file= 'papagaio.png')
button.config(image= papa)
button.config(compound= 'left')
temp = Label(window, text= tb1,
             font=('arial',10,'bold'),
             fg= 'white',
             bg= 'black',
             relief=RAISED,
             bd= '5',
             padx= '50',
             pady= '25')
temp.place(x=550,y=327)
button.place(x=0,y=320)

window.mainloop()
