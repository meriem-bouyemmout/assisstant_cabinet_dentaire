from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc
import openpyxl as Workbook
import openpyxl
import pathlib

class Assistante:
    def __init__(self,mast):
        self.master = mast
        self.master.title("Assistante Cabinet Dentaire")
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        # ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
        # ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        
        #=========================university management system=======================================#
   
        self.Frameleft = ctk.CTkFrame(self.master, width=300)
        self.Frameleft.pack(side=LEFT, fill=Y)
        #############################################################################################
        self.Nom = ctk.CTkLabel(self.Frameleft,text='Nom', font=('Helvetica',15))
        self.Nom.place(x=10,y=20 )
        self.Prenom = ctk.CTkLabel(self.Frameleft,text='Prenom', font=('Helvetica',15))
        self.Prenom.place(x=10,y=60 )
        self.Age = ctk.CTkLabel(self.Frameleft,text='Age', font=('Helvetica',15))
        self.Age.place(x=10,y=100)
        self.Motif = ctk.CTkLabel(self.Frameleft,text='Motif', font=('Helvetica',15))
        self.Motif.place(x=10,y=140 )
        self.Jour = ctk.CTkLabel(self.Frameleft,text='Jour', font=('Helvetica',15))
        self.Jour.place(x=10,y=180)
        self.Rendez_vous = ctk.CTkLabel(self.Frameleft,text='Rendez-vous', font=('Helvetica',15))
        self.Rendez_vous.place(x=10,y=220)
        self.Montant_total = ctk.CTkLabel(self.Frameleft,text='Montant total', font=('Helvetica',15))
        self.Montant_total.place(x=10,y=260)
        self.Versement = ctk.CTkLabel(self.Frameleft,text='Versement', font=('Helvetica',15))
        self.Versement.place(x=10,y=300)
        self.Reste = ctk.CTkLabel(self.Frameleft,text='Reste', font=('Helvetica',15))
        self.Reste.place(x=10,y=340)
        self.Tel = ctk.CTkLabel(self.Frameleft,text='Telephone', font=('Helvetica',15))
        self.Tel.place(x=10,y=380)
        
##################################

    


    
########################################################
        self.nom_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.nom_entry.configure(justify="center")
        self.nom_entry.place(x=120,y=20)
        self.prenom_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.prenom_entry.configure(justify="center")
        self.prenom_entry.place(x=120,y=60)
        self.age_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.age_entry.configure(justify="center")
        self.age_entry.place(x=120,y=100)
        self.motif_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.motif_entry.configure(justify="center")
        self.motif_entry.place(x=120,y=140)
        self.jour_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.jour_entry.configure(justify="center")
        self.jour_entry.place(x=120,y=180)
        self.rendez_vous_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.rendez_vous_entry.configure(justify="center")
        self.rendez_vous_entry.place(x=120,y=220)
        self.montant_total_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.montant_total_entry.configure(justify="center")
        self.montant_total_entry.place(x=120,y=260)
        self.versement_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.versement_entry.configure(justify="center")
        self.versement_entry.place(x=120,y=300)
        self.reste_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.reste_entry.configure(justify="center")
        self.reste_entry.place(x=120,y=340)
        self.tel_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12))
        self.tel_entry.configure(justify="center")
        self.tel_entry.place(x=120,y=380)


        self.buttonAdd=ctk.CTkButton(self.Frameleft,text='Ajouter', command=self.ajouter,  font=('Helvetica',10,'bold'))
        self.buttonAdd.place(x=10,y=450)

        #fichier = pathlib.Path("C:\\Users\\pc\\assist_cabinet_dentaire\\Liste_patients.xlsx")
        
        ####################################### RIGHT ####################################################
        self.Frameright = ctk.CTkFrame(self.master, height=800, fg_color='White')
        self.Frameright.pack(fill=BOTH, expand=True)
        # ##################################################################################################
        self.Framerighttop = ctk.CTkFrame(self.Frameright, height=70)
         
        # self.studentsearch = Entry(self.Framerighttop, fg='#4F4F4F', bg='white', font=('tahoma',12,'bold'), width=130)
        # self.studentsearch.grid(row = 0, column = 0, sticky='nsew', pady=10, padx=10)
        # self.buttonsearch = Button(self.Framerighttop, text='Search', command=self.search, fg='white', bg='#6E7B8B', font=('tahoma',12,'bold'), width=10)
        # self.buttonsearch.grid(row = 0, column = 1, sticky='nsew', pady=10, padx=10)
           
        self.Framerighttop.grid_columnconfigure(0, weight=1)
        self.Framerighttop.grid_columnconfigure(0, weight=1)  

        self.Framerighttop.pack(fill=X)

        ##################################################################################################
        



        self.frameView = ctk.CTkFrame(self.Frameright, height=400)
        self.frameView.pack(fill=BOTH)

        self.scrollbar = Scrollbar(self.frameView, orient = VERTICAL)
        

        self.table = ttk.Treeview(self.frameView, column= ("Nom","Prenom","Age","Motif de consultation","Jour","Rendez-vous","Montant total","Versement","Reste","Num de tel"), show='headings', height=17 , yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview())       
        self.table.pack(fill=BOTH)
         


        self.table.heading("Nom",text="Nom")
        self.table.heading("Prenom",text="Prenom")
        self.table.heading("Age",text="Age")
        self.table.heading("Motif de consultation",text="Motif de consultation")
        self.table.heading("Jour",text="Jour")
        self.table.heading("Rendez-vous",text="Rendez-vous")
        self.table.heading("Montant total",text="Montant total")
        self.table.heading("Versement",text="Versement")
        self.table.heading("Reste",text="Reste")
        self.table.heading("Num de tel",text="Num de tel")
       

        self.table.column("Nom", anchor=W, width=5)
        self.table.column("Prenom", anchor=W, width=6)
        self.table.column("Age", anchor=W, width=6)
        self.table.column("Motif de consultation", anchor=W, width=6)
        self.table.column("Jour", anchor=W, width=6)
        self.table.column("Rendez-vous", anchor=W, width=6)
        self.table.column("Montant total", anchor=W, width=6)
        self.table.column("Versement", anchor=W, width=6)
        self.table.column("Reste", anchor=W, width=6)
        self.table.column("Num de tel", anchor=W, width=6)
 

    def ajouter(self):
          nom = self.nom_entry.get()
          prenom = self.prenom_entry.get()
          age = self.age_entry.get()
          motif = self.motif_entry.get()
          jour = self.jour_entry.get()
          rendez_vous = self.rendez_vous_entry.get()
          montant_total = self.montant_total_entry.get()
          versement = self.versement_entry.get()
          reste = self.reste_entry.get()
          tel = self.tel_entry.get()

          fichier = openpyxl.load_workbook("C:\\Users\\pc\\assist_cabinet_dentaire\\Liste_patients.xlsx")
          sheet = fichier.active
          sheet.cell(column=1,row=sheet.max_row+1 , value = nom)
          sheet.cell(column=2,row=sheet.max_row , value = prenom)
          sheet.cell(column=3,row=sheet.max_row , value = age)
          sheet.cell(column=4,row=sheet.max_row , value = motif)
          sheet.cell(column=5,row=sheet.max_row , value = jour)
          sheet.cell(column=6,row=sheet.max_row , value = rendez_vous)
          sheet.cell(column=7,row=sheet.max_row , value = montant_total)
          sheet.cell(column=8,row=sheet.max_row , value = versement)
          sheet.cell(column=9,row=sheet.max_row , value = reste)
          sheet.cell(column=10,row=sheet.max_row , value = tel)
          

          fichier.save("C:\\Users\\pc\\assist_cabinet_dentaire\\Liste_patients.xlsx")  
          
          mb.showinfo('Succes ajoute','Donnees inserees', parent=self.master)

             

          self.nom_entry.delete(0,'end')
          self.prenom_entry.delete(0,'end')
          self.age_entry.delete(0,'end')
          self.motif_entry.delete(0,'end')
          self.jour_entry.delete(0,'end')
          self.rendez_vous_entry.delete(0,'end')
          self.montant_total_entry.delete(0,'end')
          self.versement_entry.delete(0,'end')
          self.reste_entry.delete(0,'end')
          self.tel_entry.delete(0,'end')



          # Load the workbook
workbook = openpyxl.load_workbook("C:\\Users\\pc\\assist_cabinet_dentaire\\Liste_patients.xlsx")

# Select the desired sheet
sheet = workbook['Sheet1']  # Replace 'Sheet1' with the name of your sheet

# Access cell values
cell_value = sheet['A1'].value  # Replace 'A1' with the desired cell address

# Iterate over rows
for row in sheet.iter_rows(min_row=2, values_only=True):
    print(row)

# Iterate over columns
for column in sheet.iter_cols(min_col=1, values_only=True):
    print(column) 




             






if (__name__ == '__main__'):
    window = ctk.CTk()
    std = Assistante(window)
    mainloop()