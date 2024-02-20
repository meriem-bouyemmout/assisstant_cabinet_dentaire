from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as mb
import Accueil as Ac


class Login :
    def __init__(self,mast):
        self.master = mast
        self.master.title("Page de connexion")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")

        self.img = Image.open('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\loginImage.png')
        self.img.thumbnail((200,200))
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgLogin = Label(self.master, image=self.new_img)
        self.imgLogin.pack(padx=50, pady = 50)

        self.frameLogin = ctk.CTkFrame(self.master,fg_color="#BCD2EE", width=100, height=100)
        self.frameLogin.pack()
        self.usernameLabel = ctk.CTkLabel(self.frameLogin, text = 'Username', pady=15, padx=25, font=('Helvetica',18))
        self.usernameLabel.grid(row=0, column=0)
        self.passwordLabel = ctk.CTkLabel(self.frameLogin, text = 'Password', pady=15, padx=25, font=('Helvetica',18))
        self.passwordLabel.grid(row=1, column=0)
        self.username = ctk.CTkEntry(self.frameLogin,  font=('tahoma',15,'bold'))
        self.username.configure(justify="center")
        self.username.grid(row=0, column=1, pady=15, padx=10)
        self.password = ctk.CTkEntry(self.frameLogin,  show='*', font=('tahoma',18,'bold'))
        self.password.configure(justify="center")
        self.password.grid(row=1, column=1, pady=15, padx=10)
        self.buttonLogin=ctk.CTkButton(self.frameLogin, text='Login', command=self.Login, height=35,  font=('Helvetica',18), cursor='cross')
        self.buttonLogin.grid(row=2, column=0, columnspan=2, sticky='snew', padx=10, pady=10)

    def Login(self):

        if(self.username.get() == 'admin' and self.password.get() == '000' ) :
                win = Toplevel()
                win.iconbitmap('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\download.ico')
                uni = Ac.Accueil(win)
                self.username.delete(0,'end')
                self.password.delete(0,'end')
           
           
   
   
   
        # if(self.username.get() == 'admin' and self.password.get() == '000' ) :
        #         win = Toplevel()
        #         win.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
        #         uni = admin(win)
        #         self.username.delete(0,'end')
        #         self.password.delete(0,'end')   
        
        # else:
        #     if (result == None) :
        #         mb.showerror('Erreur','Invalaid username and password')  
        #         self.username.delete(0,'end')
        #         self.password.delete(0,'end')
            
          

        #     else :         
        #         win = Toplevel()
        #         win.iconbitmap('C:\\Users\\pc\\Student système managment\\images\\swim_ring_icon_183313.ico')
        #         uni = University(win)
        #         self.username.delete(0,'end')
        #         self.password.delete(0,'end')   
        
        #mydb.commit()



        


             




if (__name__ == '__main__'):
    window = ctk.CTk()
    window.iconbitmap('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\download.ico')
    std = Login(window)
    mainloop()