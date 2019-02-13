# options = QFileDialog.Options()
# options |= QFileDialog.DontUseNativeDialog
#

import os
import platform
import subprocess
import tkinter as tk
from tkinter import Tk, Label, Button, StringVar
from tkinter import filedialog, messagebox




root = Tk()
root.withdraw()

folder_selected = filedialog.askdirectory(initialdir=os.getcwd(), title="Select file")


# root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                           # filetypes=[("Jpeg Files", "*.jpg")])
# print(root.filename)
print(folder_selected)
