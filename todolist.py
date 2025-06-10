# import module
from tkinter import *
from tkinter import messagebox

# create function
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning","please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# configure & create mainwindow
ws = Tk() 
ws.geometry('500x450+500+200')
ws.title('PythonGuides')
ws.config(bg = '#223441') # bg means background colour
ws.resizable(width = False, height = False)

# create widgets(frame, listbox, scrollbar, entry, button)
frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width = 25,
    height = 8,
    font = ('Times',18),
    bd = 0,
    fg = '#464646',
    highlightthickness = 0,
    selectbackground= '#a6a6a6',
    activestyle= "none",
)

lb.pack(side=LEFT,fill=BOTH)

task_list = [
    'Eat apple',
    'Drink water',
    'Go gym',
    'Study'
    'Take a book'
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times',24)
    )

my_entry.pack(pady=20)
button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text="Delete Task",
    command=deleteTask  # Ensure delete_task is defined
)
# delTask_btn.pack()  # Ensure you pack or grid the button

# delTask_btn = Button(
#     button_frame,
#     text='Delete Task',
#     FONT='times 14',
#     BG='#ff8b61',
#     padx=20,
#     pady=10,
#     command = deleteTask

# )
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()