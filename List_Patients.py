from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image,ImageTk
import tkinter.messagebox as mb
import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import pathlib
import sqlite3
from tkinter import filedialog

class List_Patients:
    def __init__(self,mast):
        self.master = mast
        self.master.title("Les patients")
        ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state("zoomed")
        
        
        
        #=========================university management system=======================================#
   
        self.Frameleft = ctk.CTkFrame(self.master,fg_color="#BCD2EE", width=300)
        self.Frameleft.pack(side=LEFT, fill=Y)
        ################################################################################################
       

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
        
        self.nom = StringVar()
        self.prenom = StringVar()
        self.age = StringVar()
        self.motif = StringVar()
        self.jour = StringVar()
        self.rendez_vous = StringVar()
        self.montant_ttl = StringVar()
        self.versement = StringVar()
        self.reste = StringVar()
        self.num_de_tel = StringVar()

    


    
########################################################
        self.nom_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.nom)
        self.nom_entry.configure(justify="center")
        self.nom_entry.place(x=120,y=20)
        self.prenom_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.prenom)
        self.prenom_entry.configure(justify="center")
        self.prenom_entry.place(x=120,y=60)
        self.age_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.age)
        self.age_entry.configure(justify="center")
        self.age_entry.place(x=120,y=100)
        self.motif_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.motif)
        self.motif_entry.configure(justify="center")
        self.motif_entry.place(x=120,y=140)
        self.jour_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.jour)
        self.jour_entry.configure(justify="center")
        self.jour_entry.place(x=120,y=180)
        self.rendez_vous_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.rendez_vous)
        self.rendez_vous_entry.configure(justify="center")
        self.rendez_vous_entry.place(x=120,y=220)
        self.montant_total_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.montant_ttl)
        self.montant_total_entry.configure(justify="center")
        self.montant_total_entry.place(x=120,y=260)
        self.versement_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable = self.versement)
        self.versement_entry.configure(justify="center")
        self.versement_entry.place(x=120,y=300)
        self.reste_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable =self.reste)
        self.reste_entry.configure(justify="center")
        self.reste_entry.place(x=120,y=340)
        self.tel_entry = ctk.CTkEntry(self.Frameleft, font=('tahoma',12), textvariable =self.num_de_tel)
        self.tel_entry.configure(justify="center")
        self.tel_entry.place(x=120,y=380)


        self.buttonAdd=ctk.CTkButton(self.Frameleft,text='Ajouter', command=self.ajouter,  font=('Helvetica',15,'bold'))
        self.buttonAdd.place(x=10,y=450)
        self.buttonDELETE=ctk.CTkButton(self.Frameleft,text='Supprimer', command=self.delete,  font=('Helvetica',15,'bold'))
        self.buttonDELETE.place(x=155,y=450)
        self.buttonUP=ctk.CTkButton(self.Frameleft,text='Mise a jour', command=self.update,  font=('Helvetica',15,'bold'))
        self.buttonUP.place(x=10,y=485)
        self.buttonRESET=ctk.CTkButton(self.Frameleft,text='Nettoyer', command=self.netoyer,  font=('Helvetica',15,'bold'))
        self.buttonRESET.place(x=155,y=485)


        image_path = "C:\\Users\\pc\\assist_cabinet_dentaire\\images\\download-_1_.ico"
        image = Image.open(image_path)    
        image = image.resize((30, 30))
        photo_image = ImageTk.PhotoImage(image)



        self.buttonEXCEL=ctk.CTkButton(self.Frameleft, image=photo_image, text='Exporter vers excel', command=self.export_to_excel,height=40,  font=('Helvetica',15,'bold'))
        self.buttonEXCEL.place(x=10,y=550)

        #fichier = pathlib.Path("C:\\Users\\pc\\assist_cabinet_dentaire\\Liste_patients.xlsx")
        
        ####################################### RIGHT ####################################################
        self.Frameright = ctk.CTkFrame(self.master, height=800)
        self.Frameright.pack(fill=BOTH, expand=True)
        ###########################################################################################################
        


        # ##################################################################################################
        self.Framerighttop = ctk.CTkFrame(self.Frameright,fg_color="#BCD2EE", height=70)
         
        self.rechercher_entry = ctk.CTkEntry(self.Framerighttop,  font=('Helvetica',18,'bold'), width=10)
        self.rechercher_entry.grid(row = 0, column = 0, sticky='nsew', pady=10, padx=5)
        self.rechercher_button = ctk.CTkButton(self.Framerighttop, text='Rechercher', command=self.rechercher_ligne_par_valeur, font=('Helvetica',16,'bold'), height=35)
        self.rechercher_button.grid(row = 0, column = 1, sticky='nsew', pady=10, padx=5)
        self.voir_button = ctk.CTkButton(self.Framerighttop, text='Voir', command=self.voir, font=('Helvetica',16,'bold'), height=35)
        self.voir_button.grid(row = 0, column = 2, sticky='nsew', pady=10, padx=5)
           
        self.Framerighttop.grid_columnconfigure(0, weight=1)
        self.Framerighttop.grid_columnconfigure(0, weight=1)  

        self.Framerighttop.pack(fill=X)

        ##################################################################################################
        
        


        self.frameView = ctk.CTkFrame(self.Frameright, height=400)
        self.frameView.pack(fill=BOTH)

        self.scrollbar = Scrollbar(self.frameView, orient = VERTICAL)

        style1 = ttk.Style()
        style1.layout('my.treeview.layout',
                    [('Header', {'sticky':'nswe'})] +
                    [('Separator', {'sticky':'ew'})] +
                    [('Item..focus', {'sticky':'nswe'})] +
                    [('Item', {'sticky':'nswe'})]
                    )
        style1.configure("Treeview",  background="#00C957")
        style1.configure("Treeview.Item", font=("Helvetica", 12))
        style1.configure("Treeview.Heading",  font=("tahoma", 10))

        

        self.table = ttk.Treeview(self.frameView, style='Treeview.Heading', column= ("ID","Nom","Prenom","Age","Motif de consultation","Jour","Rendez-vous","Montant total","Versement","Reste","Num de tel"), show='headings', height=17 , yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.table.yview())       
        self.table.pack(fill=BOTH)
         

        self.table.heading("ID",text="ID")
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
       
        self.table.column("ID", anchor=W, width=5)
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
        
        # style = ttk.Style()
        # style.theme_use("default")
        # style.configure("Treeview", background='',filedbackground=)
        # style.configure("Treeview.Heading", foreground="green", font=("tahoma", 10))

        

        
        self.lire()
        self.table.bind("<ButtonRelease>", self.show)
        

        self.img = Image.open('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\Teethcare Health Concept with Dental Care Tools and Dentist Instruments Stock Image - Image of health, dentistry_ 157806363.jpg')
        self.new_img = ImageTk.PhotoImage(self.img)
        self.imgDent = Label(self.Frameright, image=self.new_img)
        self.imgDent.pack( padx=0, pady =0)

        # self.img = Image.open('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\Premium Photo _ Dentist mirror and a tooth model on pastel green color background 3d illustration.jpg')
        # self.img.thumbnail((200,200))
        # self.new_img = ImageTk.PhotoImage(self.img)
        # self.imgLogin = Label(self.Frameright, image=self.new_img)
        # self.imgLogin.pack(padx=10, pady =10) 

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

          # Connect to SQLite database
          conn = sqlite3.connect("data_base.db")
          cursor = conn.cursor()

          # Fetch data from SQLite
          

          if (nom == '' or prenom == '' ) :
           mb.showerror('Erreur','Veuiller saisir le nom et le prenom', parent=self.master)
          else :
              req = "INSERT INTO Patient(Nom, Prenom, Age, Motif, Jour, Rendez_vous, Montant_total, Versement, Reste, Num_de_tel) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"  
              val = (nom, prenom, age, motif, jour, rendez_vous, montant_total, versement, reste, tel)          
              cursor.execute(req, val)        
              conn.commit()
              conn.close() 
              mb.showinfo('Succes ajoute','Donnees inserees', parent=self.master)
              self.lire()          
              self.netoyer()

       
   
    def lire(self):
          
          # Connect to SQLite database
          conn = sqlite3.connect("data_base.db")
          cursor = conn.cursor()

          # Fetch data from SQLite
          #req = "SELECT Nom, Prenom, Age, Motif, Jour, Rendez_vous, Montant_total, Versement, Reste, Num_de_tel FROM Patient" 
          cursor.execute("SELECT * FROM Patient")
          data = cursor.fetchall()

  
          self.table.delete(*self.table.get_children())

          counter = 1  # Start from 1 or another appropriate value
          for i in data:
            self.table.insert('', 'end', iid=str(counter), values=i)
            counter += 1
 
          conn.close()  
              
    def show(self,ev): 
        selected_item = self.table.selection()
    
        # Extract the unique identifier (e.g., ID)
        self.row_id = self.table.item(selected_item, "values")[0]

        self.data = self.table.focus()
        alldata = self.table.item(self.data)
        print(self.row_id)
        val = alldata['values']
        self.nom.set(val[1])
        self.prenom.set(val[2])
        self.age.set(val[3])
        self.motif.set(val[4])
        self.jour.set(val[5])
        self.rendez_vous.set(val[6])
        self.montant_ttl.set(val[7])
        self.versement.set(val[8])
        self.reste.set(val[9])
        self.num_de_tel.set(val[10])

    def voir(self):
        # Call your read function to refresh the table with all data
        self.lire()

        # Optionally, you can clear the search entry if you have one
        self.rechercher_entry.delete(0, 'end')

    def netoyer(self):
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


    def delete(self):
    
        # Connect to SQLite database
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()
        req = ("delete from patient where ID="+self.row_id)
        cursor.execute(req)
        conn.commit()
        conn.close()
        mb.showinfo('Supprimer', 'Le patient a été supprimé', parent=self.master)
        self.lire()
        self.netoyer() 

    def update(self):
      
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

        # print(nom, prenom, age, motif, jour, rendez_vous, montant_total, versement, reste, tel )  
        
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()

        if (nom == '' or prenom == '' ) :
           mb.showerror('Erreur','Veuiller saisir le nom et le prenom', parent=self.master)
        else :
              req = "UPDATE Patient set ID=? ,Nom=?, Prenom=?, Age=?, Motif=?, Jour=?, Rendez_vous=?, Montant_total=?, Versement=?, Reste=?, Num_de_tel=? WHERE ID=? "  
              val = (self.row_id, nom, prenom, age, motif, jour, rendez_vous, montant_total, versement, reste, tel, self.row_id)          
              cursor.execute(req, val)        
              conn.commit()
              conn.close() 
              mb.showinfo('Mise a jour','Le patient a été mis à jour', parent=self.master)
              self.lire()          
              self.netoyer()
        

    def rechercher_ligne_par_valeur(self):

        rechercher_entry = self.rechercher_entry.get()
        conn = sqlite3.connect("data_base.db")
        cursor = conn.cursor()

    # Remplacez 'nom_de_la_table' par le nom réel de votre table et 'nom_colonne' par le nom de la colonne dans laquelle vous voulez rechercher.
        req = (f"SELECT * FROM Patient WHERE Nom LIKE ?")
        cursor.execute(req, ('%' + rechercher_entry + '%',))

    # Utilisation du caractère joker '%' pour rechercher partiellement la valeur
        resultats = cursor.fetchall()
        print(resultats)
        if  not resultats: 
    
            req2 = (f"SELECT * FROM Patient WHERE Prenom LIKE ?")
            cursor.execute(req2, ('%' + rechercher_entry + '%',))

            # Utilisation du caractère joker '%' pour rechercher partiellement la valeur
            resultats2 = cursor.fetchall()
            
            if  not resultats2:
            
                mb.showerror("Erreur","Le patient n'existe pas ", parent=self.master) 
                print(resultats2)

            else : 

                # Effacer les anciennes entrées dans le tableau
                for row in self.table.get_children():
                    self.table.delete(row)

                # Afficher les résultats dans le tableau
                for resultat in resultats2:
                    self.table.insert("", "end", values=resultat)   
        
        else :

            # Effacer les anciennes entrées dans le tableau
            for row in self.table.get_children():
                self.table.delete(row)

            # Afficher les résultats dans le tableau
            for resultat in resultats:
                self.table.insert("", "end", values=resultat)

        conn.commit()
        conn.close() 



    def export_to_excel(self):
        
            # Connect to SQLite database
            conn = sqlite3.connect("data_base.db")
            cursor = conn.cursor()

            # Fetch data from SQLite
            cursor.execute("SELECT * FROM patient")
            data = cursor.fetchall()

            # Create a new Excel workbook and sheet
            wb = Workbook()
            ws = wb.active

            # Write headers to Excel sheet
            headers = [description[0] for description in cursor.description]
            ws.append(headers)

            # Write data to Excel sheet
            for row in data:
                ws.append(row)

            # Save Excel file
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                wb.save(file_path)
                mb.showinfo("Export Successful", f"Data exported to {file_path}", parent=self.master)
            
            conn.close()
        


if (__name__ == '__main__'):
    window = ctk.CTk()
    window.iconbitmap('C:\\Users\\pc\\assist_cabinet_dentaire\\images\\download.ico')
    std = List_Patients(window)
    mainloop()