#sample program to encrypt a text file.
from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet

class code:
    file=''
    # Function for opening the file explorer window
    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files","*.txt*"),
                                                       ("all files","*.*")))
        # Change label contents
        label_file_explorer.configure(text="File Opened: "+filename)
        code.file=filename
    #encryption function
    def fun1(self):
         #Get the key from the file
         fil=open('key.txt','rb')
         key=fil.read()
         fil.close()
         #Encode the file
         text=open(code.file).read()
         encoded=text.encode()
         #Encrypt the file
         f=Fernet(key)
         encrypted=f.encrypt(encoded)
         f1=open(code.file[0:len(code.file)-4]+'_Encrypted.txt','wb')
         f1.write(encrypted)
         f1.close()
         # Change label contents
         label_file_explorer.configure(text="Your file has been successfully encrypted.Click on 'Browse File' below to encrypt another file,\nelse close the application.")

def gen_key():
        key=Fernet.generate_key()
        print(key)
        file=open('key.txt','wb')
        file.write(key)
        file.close()
gen_key()
a=code()

window=Tk()
window.iconphoto(False,PhotoImage(file='A.png'))
window.title("File Encryption")
window.geometry("500x300")
window.config(background = "pink")
window.resizable(width=False, height=False)

# Create a File Explorer label
label_name = Label(window,
                   text = "Cryptography Tool",
                   width =50, height = 4,
                   background='#ffff99',
                   font =('Verdana', 12),
                   fg = "green")

label_file_explorer = Label(window,
                            text = "File Explorer",
                            width = 71, height = 4,
                            background='#c6ffb3',
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse File",
                        width=25,
                        height=2,
                        relief='groove',
                        command = a.browseFiles)
  
button_exit = Button(window,
                     text = "submit",
                     width=15,
                     height=2,
                     relief='raised',
                     bg='#ccccb3',
                     command = a.fun1)


label_about = Label(window,
                    text = "© The Code Men\n2022",
                    width = 71, height = 5,
                    background='#99ccff',
                    fg = "black")
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_name.grid(column = 1, row = 1)

label_file_explorer.grid(column = 1, row = 2)
  
button_explore.grid(column = 1, row = 3)
  
button_exit.grid(column = 1,row = 4)

label_about.grid(column = 1, row = 5)
window.mainloop()

