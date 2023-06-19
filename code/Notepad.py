from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

root = Tk()
root.title("James Notepad")
root.geometry("500x500")

text = Text(root)
text.focus_force()
text.pack(fill="both", expand=True)

def open_file():
    file_path = askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", "end")
            file.write(content)

def about():
    messagebox.showinfo(message="App made by @James, feel free to use")

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_about = Menu(menu)
menu.add_cascade(label="About", menu=file_about)
file_about.add_command(label="creator", command=about)
file_about.add_separator()

root.mainloop()
