from tkinter import *
from tkinter import Menu
window=Tk()
window.title("Restarant control")
#window.resizable(True,True)
menu = Menu(window)
new_item = Menu(menu)

new_item.add_command(label='Login')

new_item.add_separator()

new_item.add_command(label='Configuration')

menu.add_cascade(label='Options', menu=new_item)

window.config(menu=menu)




title=Label(text="RESTAURANT CONROL",justify="center")
title.pack()
text=Text(window)
email=Entry()
password=Entry()
email.pack()
password.pack()






# Configure the alignment of the text
text.tag_configure("tag_name", justify='center')

# Insert a Demo Text
text.insert("1.0", "How do I center align the text " "in a Tkinter Text widget?")

# Add the tag in the given text
text.tag_add("tag_name", "1.0", "end")
text.pack()

window.mainloop()
