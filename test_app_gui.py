import os
import platform
import subprocess
import tkinter as tk
from tkinter import Tk, Label, Button, StringVar
from tkinter import filedialog, messagebox

# root = Tk()
# root.withdraw()
#
#
# folder_selected = filedialog.askdirectory(initialdir=os.getcwd(), title="Select file",
#                                            filetypes=[("Jpeg Files", "*.jpg")])
#
#


### Xloc = 580, Yloc = 380




def OnFocusIn(event):
    if type(event.widget).__name__ == 'Tk':
        event.widget.attributes('-topmost', False)

# Create and configure your root ...

root = Tk()
root.title('Auto Culling GUI')
root.resizable(False, False)  # This code helps to disable windows from resizing


# root.attributes('-topmost', True)
# root.focus_force()
# root.bind('<FocusIn>', OnFocusIn)

tk.Label(root, text="WELCOME").pack()
# tk.Button(root, text="Don't test me Tony").pack()

# cool_frame = tk.Frame(root)
# cool_frame.pack()
#
# label2 = tk.Label(cool_frame, text='label #2')
# label2.pack()


window_height = 500
window_width = 900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# messagebox.showinfo("Title", "a Tk MessageBox")
messagebox.showinfo("Information", "Welcome to the Automated Cullin App")

root.attributes('-topmost', True)
root.focus_force()
root.bind('<FocusIn>', OnFocusIn)

# root.directory = filedialog.askdirectory()
# print (root.directory)

root.mainloop()






# class MyFirstGUI:
#     LABEL_TEXT = [
#         "This is our first GUI!",
#         "Actually, this is our second GUI.",
#         "We made it more interesting...",
#         "...by making this label interactive.",
#         "Go on, click on it again.",
#     ]
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#
#         self.label_index = 0
#         self.label_text = StringVar()
#         self.label_text.set(self.LABEL_TEXT[self.label_index])
#         self.label = Label(master, textvariable=self.label_text)
#         self.label.bind("<Button-1>", self.cycle_label_text)
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
#     def cycle_label_text(self, event):
#         self.label_index += 1
#         self.label_index %= len(self.LABEL_TEXT) # wrap around
#         self.label_text.set(self.LABEL_TEXT[self.label_index])
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()




















######################## NOTES BELOW THIS LINE ##############################

# win = tk.Tk()  # Creating instance of Tk class
# win.title("Centering windows")
# win.resizable(False, False)  # This code helps to disable windows from resizing
#
# window_height = 500
# window_width = 900
#
# screen_width = win.winfo_screenwidth()
# screen_height = win.winfo_screenheight()
#
# x_cordinate = int((screen_width/2) - (window_width/2))
# y_cordinate = int((screen_height/2) - (window_height/2))
#
# win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#
# win.mainloop()


# def raise_app(root: Tk):
#     root.attributes("-topmost", True)
#     if platform.system() == 'Darwin':
#         tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
#         script = tmpl.format(os.getpid())
#         output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
#     root.after(0, lambda: root.attributes("-topmost", False))
#
#
# # You call it right before the mainloop() call, like so:
# raise_app(root)
# root.mainloop()
