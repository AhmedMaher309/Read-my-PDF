import PyPDF2
import pyttsx3
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import webbrowser

# initialisation of the pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 165)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

file=""
# Function for opening the file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"),("PDF files", "*.pdf*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	webbrowser.open_new(filename)
	global file
	file=filename

# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("700x500")

#Set window background color
window.config(background = "white")


# Create a File Explorer label
label_file_explorer = Label(window, text = "File Explorer using Tkinter", width = 100, height = 4, fg = "blue")

	
button_explore = Button(window, text = "Browse Files", command = browseFiles)

button_exit = Button(window, text = "Read PDf", command = window.destroy)

# Grid method is chosen for placing the widgets at respective positions in a table like structure by specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()

# creating a pdf file object
pdfFileObj = open(file, 'rb')
	
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# get the number of pages
pages=pdfReader.numPages
for x in range(0,pages):
   # creating an object for each page
   pageObj = pdfReader.getPage(x)

  # extract the text in each page
   mytext = pageObj.extractText(x)
   engine.say(mytext)
 
engine.runAndWait()

# close the pdf file object
pdfFileObj.close()


  
