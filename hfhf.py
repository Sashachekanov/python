from tkinter import *
from tkinter import ttk
root = Tk()
root.title('METANIT.COM')
root.geometry('250x200')

people = [('Tom', 38, 'tom@gmail.com'), ('Bob', 42, 'bob@gmail.com'), ('Sam', 28, 'sam@gmail.com')]

columns = ('name', 'age', 'gmail')

tree = ttk.Treeview(columns=columns, show='headings')
tree.pack(fill=BOTH, expand=1)

