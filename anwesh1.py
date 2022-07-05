from tkinter import * 
from tkinter import messagebox 
import math,random,os 

class Bill_App:    
    def __init__(self,root): 
        self.root=root 
        self.root.geometry("1350x700+0+0") 
        self.root.title("Billing Software") 
        bg_color="#074463" 
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X) 


        #=============Variables====================== 
        #=============Cosmetics====================== 
        self.soap=IntVar() 
        self.face_cream=IntVar() 
        self.face_wash=IntVar()
        self.spray=IntVar() 
        self.gel=IntVar() 
        self.lotion=IntVar() 


        #=============Grocery======================== 
        self.rice=IntVar() 
        self.food_oil=IntVar()  
        self.daal=IntVar() 
        self.wheat=IntVar() 
        self.sugar=IntVar()
        self.tea=IntVar() 


        #=============Cold Drinks==================== 
        self.maaza=IntVar() 
        self.coke=IntVar() 
        self.frooti=IntVar() 
        self.thumbsup=IntVar() 
        self.limca=IntVar() 
        self.sprite=IntVar() 

 
        #=============Total Product Price and Tax variables==================== 
        self.cosmetic_price=StringVar() 
        self.grocery_price=StringVar() 
        self.cold_drink_price=StringVar() 
        self.cosmetic_tax=StringVar() 
        self.grocery_tax=StringVar() 
        self.cold_drink_tax=StringVar() 


        #=============Customer Detail================ 
        self.c_name=StringVar() 
        self.c_phon=StringVar() 
        self.bill_no=StringVar()
        x=random.randint(1000,9999) 
        self.bill_no.set(str(x)) 
        self.search_bill=StringVar() 

