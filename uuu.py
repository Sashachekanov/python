from tkinter import *


root = Tk()
root.title('Номерная книга')
root.geometry('300x550')

tx = Entry()
tx.grid(column=0, row=0)
txt = Entry()
txt.grid(column=0, row=1)
def f():
    print(tx.get(), txt.get())
    label["text"] = tx.get()
    label1['text']=txt.get()




btn = Button(text='Записать', command=f)
btn.grid(column=1, row=0)
# n = Button(text='Записать')
# n.grid(column=1, row=1)

label = Label()
label1=Label()
label.grid(column=0, row=2)
label1.grid(column=5, row=2)



root.mainloop()
