from tkinter import *
from tkinter import messagebox

app = Tk()

varInputA = StringVar()
varInputB = StringVar()


def tambah():
    hasil = int(varInputA.get()) + int(varInputB.get())
    messagebox.showinfo(message=str(hasil))


def kurang():
    hasil = int(varInputA.get()) - int(varInputB.get())
    messagebox.showinfo(message=str(hasil))


def kali():
    hasil = int(varInputA.get()) * int(varInputB.get())
    messagebox.showinfo(message=str(hasil))


def bagi():
    hasil = int(varInputA.get()) / int(varInputB.get())
    messagebox.showinfo(message=str(hasil))


app.geometry('300x200')
app.title('Aplikasi Kalkulator')
app.configure(bg='purple')
Label(app, text='APLIKASI KALKULATOR', bg='purple',
      foreground='white').place(x=85, y=25)
Label(app, text='Masukkan angka', bg='purple',
      foreground='white').place(x=5, y=55)
Entry(app, textvariable=varInputA, width=15).place(x=115, y=55)

Label(app, text='Masukkan angka', bg='purple',
      foreground='white').place(x=5, y=85)
Entry(app, textvariable=varInputB, width=15).place(x=115, y=85)

Button(app, text='+', bg='green', foreground='white',
       width=5, command=tambah).place(x=10, y=115)
Button(app, text='-', bg='red', foreground='white',
       width=5, command=kurang).place(x=70, y=115)
Button(app, text='x', bg='salmon', foreground='white',
       width=5, command=kali).place(x=130, y=115)
Button(app, text=':', bg='blue', foreground='white',
       width=5, command=bagi).place(x=190, y=115)
app.mainloop()
