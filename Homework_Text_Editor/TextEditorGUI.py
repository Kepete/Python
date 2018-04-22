from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText

window = Tk (className = " Python Text Editor by Kepete")
textArea = ScrolledText.ScrolledText(window, width=100, height=30)

# Create functions:

def openFile():
	file = filedialog.askopenfile(parent = window, mode = "rb", title = "Select text file: ")

	if file != None: 
		contents = file.read()
		textArea.insert("1.0", contents) # Starting from line 1 to the end of content
		file.close() 


def saveFile():
	file = filedialog.asksaveasfile(mode = "w")

	if file != None:
		data = textArea.get("1.0", END) 
		file.write(data)
		file.close()

def closeProgram():
	window.destroy()


def aboutProgram():
	messagebox.showinfo("About", "This is a text editor program that was created as a homework by Ken-Tristan Peterson. \n  \nVersion 1.0.0 ")	

def FAQhelp():
	messagebox.showinfo("Frequently Asked Questions", "Why doesn't the program save the file with .txt extension? \n  \nWhile saving you can choose the file extension by adding the extension to the file name. \nFor example: FileName.txt ")

# Create menu options:
menu = Menu(window)
window.config(menu = menu)
fileMenu = Menu(menu)
helpMenu = Menu(menu)

menu.add_cascade(label = "File", menu = fileMenu) # Creates a new hierarchical menu by associating a given menu to a parent menu
fileMenu.add_command(label = "Open", command = openFile) # Adds a menu item to the fileMenu
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_separator() # Line between menu items
fileMenu.add_command(label = "Close", comman = closeProgram)

menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "FAQ", command = FAQhelp)
helpMenu.add_command(label = "About", command = aboutProgram)


textArea.pack()

window.mainloop() # Holds window open