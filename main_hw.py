from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

mainWin=Tk()
mainWin.title('Student marks populating app')
mainWin.geometry("600x400")

my_studentmarks = {}

def delete():
    select = book_list.curselection()
    key = book_list.get(select)
    del my_studentmarks[key]
    book_list.delete(select)
    clear_all()

def clear_all():
    name.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

def edit():
    clear_all()
    select = book_list.curselection()
    key = book_list.get(select)
    details = my_studentmarks[key]
    name.insert(0,key)
    entry2.insert(0,details[0])
    entry.insert(0,details[1])
    entry3.insert(0,details[2])
    entry4.insert(0,details[3])

def add():
    name2 = name.get()
    if name2 not in my_studentmarks.keys():
        book_list.insert(END,name2)
    my_studentmarks[name2] = (entry.get(),entry2.get(),entry3.get(),entry4.get())
    clear_all()


def save():
    file = asksaveasfile(defaultextension=".txt")
    if file is not None:
        print(my_studentmarks,file=file)
        my_studentmarks.clear()
        messagebox.showinfo("saved","Your file has been saved")


bookName = Label(mainWin, text='My Student marks',width=35)
bookName.grid(row = 0, column = 1,pady = 10,columnspan=3)

book_list =Listbox(mainWin,height=15,width=30)
book_list.grid(row = 2, column = 0,columnspan=3, rowspan = 5)

name_label =Label(mainWin, text = 'Student name:')
name_label.grid(row= 2, column = 3)
name =Entry(mainWin)
name.grid(row = 2, column = 4,padx=5)

mark1_label =Label(mainWin, text = 'Mark 1:')
mark1_label.grid(row = 3, column = 3)
entry2 =Entry(mainWin)
entry2.grid(row = 3, column = 4,padx=5)

mark2_label =Label(mainWin, text = 'Mark 2')
mark2_label.grid(row = 4, column = 3)
entry =Entry(mainWin)
entry.grid(row = 4, column = 4,padx=5)

total_label = Label(mainWin, text = 'Total:')
total_label.grid(row = 5, column = 3)
entry3 =Entry(mainWin)
entry3.grid(row = 5, column = 4,padx=5)

grade_label = Label(mainWin, text = 'Grade:')
grade_label.grid(row = 6, column = 3)
entry4 = Entry(mainWin)
entry4.grid(row =6, column = 4,padx=5)


Edit_button = Button(mainWin, text = 'Edit',width=10,command=edit)
Edit_button.grid(row = 7, column = 0, padx = 12,pady=12) 

delete_button =Button(mainWin, text = 'Delete',width=10,command=delete)
delete_button.grid(row = 7, column = 1,pady=12 )

add_button =Button(mainWin, text = 'Update/Add',command=add)
add_button.grid(row = 7, column = 4,pady=12)

save_button = Button(mainWin, text='Save',width=35)
save_button.grid(row = 8, column = 1,pady = 10,columnspan=3)

mainWin.mainloop()