from tkinter import *
from backend import Database

database=Database("movie.db")

def gettherow(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def delete_command():
    database.delete(selected_tuple[0])
    view_command()





def view_command():
    listbox.delete(0,END)
    for row in database.view():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    for row in database.search(title_text.get(),director_text.get(),year_text.get(),grade_text.get()):
        listbox.insert(END,row);

def add_command():
    database.insert(title_text.get(),director_text.get(),year_text.get(),grade_text.get())
    listbox.delete(0,END)
    listbox.insert(END,(title_text.get(),director_text.get(),year_text.get(),grade_text.get()))
    view_command()

def update_command():
    database.update(selected_tuple[0],title_text.get(),director_text.get(),year_text.get(),grade_text.get())
    view_command()

window=Tk()
window.wm_title("Movies Grade")

#-----------lABELS-----------------
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Director")
l2.grid(row=1,column=0)

l3=Label(window,text="Year")
l3.grid(row=2,column=0)

l4=Label(window,text="Grade")
l4.grid(row=3,column=0)
#-----------------------------------
#-------ENTRIES---------------------
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

director_text=StringVar()
e2=Entry(window,textvariable=director_text)
e2.grid(row=1,column=1)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=2,column=1)

grade_text=StringVar()
e4=Entry(window,textvariable=grade_text)
e4.grid(row=3,column=1)
#-----------------------------------------------
#---------------LISTBOX&SCROLLBAR-------------------
listbox=Listbox(window,height=8,width=45)
listbox.grid(row=4,column=0,rowspan=7,columnspan=3)

scrollbar=Scrollbar(window)
scrollbar.grid(row=4,column=3,rowspan=7)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>',gettherow)
#---------------------------------------------------
#-------------BUTTONS-------------------------------
b1=Button(window,text="View All",width=16,command=view_command)
b1.grid(row=0,column=4,rowspan=2)
b1.configure(bg="blue",fg="white")

b2=Button(window,text="Add Entry",width=16,command=add_command)
b2.grid(row=2,column=4,rowspan=2)
b2.configure(bg="green",fg="white")

b3=Button(window,text="Update",width=16,command=update_command)
b3.grid(row=5,column=4)
b3.configure(bg="grey",fg="black")

b4=Button(window,text="Delete",width=16,command=delete_command)
b4.grid(row=6,column=4)
b4.configure(bg="red",fg="black")

b5=Button(window,text="Search",width=16,command=search_command)
b5.grid(row=7,column=4)
b5.configure(bg="orange",fg="white")


b6=Button(window,text="Close",width=16,command=window.destroy)
b6.grid(row=8,column=4)
b6.configure(bg="black",fg="white")

#---------------------------------------------------

window.mainloop()
