import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

box = tk.Entry(window,width=10)
box.place(x=340,y=70)

box2 = tk.Entry(window,width=10)
box2.place(x=340,y=100)

box3 = tk.Entry(window,width=10)
box3.place(x=340,y=130)

box4 = tk.Entry(window,width=10)
box4.place(x=340,y=160)

box5 = tk.Entry(window,width=10)
box5.place(x=340,y=190)

button = tk.Button(window, text = "Update/Add", background = "White")
button.place(x=340,y=220)

button = tk.Button(window, text = "Save", background = "White")
button.place(x=220,y=400)

button = tk.Button(window, text = "Edit", background = "White")
button.place(x=50,y=340)

button = tk.Button(window, text = "Delete", background = "White")
button.place(x=140,y=340)

label = tk.Label(window, text = "Name:", background = "Black")
label.place(x=290,y=70)

label = tk.Label(window, text = "Address:", background = "Black")
label.place(x=280,y=100)

label = tk.Label(window, text = "Mobile:", background = "Black")
label.place(x=290,y=130)

label = tk.Label(window, text = "Email:", background = "Black")
label.place(x=290,y=160)

label = tk.Label(window, text = "Birthday:", background = "Black")
label.place(x=280,y=190)






















window.mainloop()
