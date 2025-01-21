import tkinter

window=tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=500,height=500)
def click_button():
    print("button clicked")
    user_input=my_entry.get()
    print(user_input )
#label

label=tkinter.Label(text="This is a label",font=('Cebri',20,'bold'))
label.config(bg="black",fg="white")
label.pack()
label.grid(row=0,column=0)

#button
my_button=tkinter.Button(text="Button for running",command=click_button,bg="Blue")
#my_button.pack(side="left")
#my_button.place(x=10, y=100)
my_button.grid(row=1,column=0 )
#entry
my_entry=tkinter.Entry(width=30, )
#my_entry.pack(side="right")
#my_entry.place(x=175,y=100)


window.mainloop()