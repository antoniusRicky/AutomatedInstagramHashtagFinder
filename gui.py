from tkinter import *
from hashtag_search import searchTopic

# USEFUL FUNCTIONS
def isInputValid():
    topic = ent_topic.get()
    if topic.isalpha():
        return True
    return False

def buttonClicked():
    if isInputValid():
        lbl_test = Label(root, text = "Valid, you entered: " + ent_topic.get())
        searchTopic(ent_topic.get())
    else:
        lbl_test = Label(root, text = "Invalid")
    lbl_test.grid()
    ent_topic.delete(0, END)

# GUI PART
root = Tk()
root.title("InstaHash")

ent_topic = Entry(root)

lbl_title = Label(root, text = "Automated Instagram Hashtag Finder")
lbl_insert = Label(root, text = "Insert your topic here")
lbl_warning = Label(root, text = "Make sure your input does not contain numbers, symbols, and whitespaces")
btn_search = Button(root, text = "Search!", command = buttonClicked)

lbl_title.grid()
ent_topic.grid()
btn_search.grid()
lbl_warning.grid()

root.mainloop()
