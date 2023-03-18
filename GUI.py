from tkinter import *
import main





root = Tk()




button1 = Button(root, text="Scrap", command=main.onClick)
frame1 = LabelFrame(root, text="data", background="green")

label1 = Label(frame1, text="hello guys!!")
label1.pack()

frame1.place(x=20,y=20)


button1.place(x=80, y=80)




root.mainloop()