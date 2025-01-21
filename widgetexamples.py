from tkinter import*

window=Tk()
window.title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=15,pady=15)

label =Label(text="my label")
label.config(bg="black",)
label.config(fg="white")
label.config(padx=10,pady=10)
label.pack()

def Button_click():
    print("Button")
    user_input= text.get("1.0",END)#1.0 hangi satır ve karakter den başladığımızı anlatıyor.
    print(user_input) # text ten çekmek istersen index atamalısın.
                             # entry için işe index e gerek yok.
button = Button(text="Button",command=Button_click)
button.pack()

entry= Entry(width=30)
entry.pack()

text=Text(width=20,bg="white",height=8)
text.focus() # direk text den başlatıyor mouse u.
text.pack()

#scale
def scale_selected(value):
    print(value)
my_scale=Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox=Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

def checkbutton_selected():
    print(check_state.get())

check_state = IntVar() # check buttton seçldiyse 1 seçilmediyse 0 verir.
my_checkbutton=Checkbutton(text="Check",variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

window.mainloop()

