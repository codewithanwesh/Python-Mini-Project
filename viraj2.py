    def save_bill(self): 
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?") 
        if op>0: 
            self.bill_data=self.textarea.get('1.0',END) 
            f1=open("D:\\project\\bill_app\\invoice\\"+str(self.bill_no.get())+".txt","w") 
            f1.write(self.bill_data) 
            f1.close() 
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfullt") 
        else: 
            return 
    
    def find_bill(self): 
        present="no" 
        for i in os.listdir("D:\\project\\bill_app\\invoice\\"): 
            if i.split(".")[0]==self.search_bill.get(): 
                f1=open(f"D:\\project\\bill_app\\invoice\\{i}","r") 
                self.textarea.delete('1.0',END) 
                for d in f1:
                    self.textarea.insert(END,d) 
                f1.close() 
                present="yes" 
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No") 
    def clear_data(self): 
        op=messagebox.askyesno("clear","Do you want to Reset Entries?") 

        if op>0: 


            #=============Cosmetics====================== 
            self.soap.set(0) 
            self.face_cream.set(0) 
            self.face_wash.set(0) 
            self.spray.set(0) 
            self.gel.set(0) 
            self.lotion.set(0) 


            #=============Grocery======================== 
            self.rice.set(0) 
            self.food_oil.set(0)  
            self.daal.set(0) 
            self.wheat.set(0) 
            self.sugar.set(0) 
            self.tea.set(0) 


            #=============Cold Drinka==================== 
            self.maaza.set(0) 
            self.coke.set(0) 
            self.frooti.set(0) 
            self.thumbsup.set(0) 
            self.limca.set(0) 
            self.sprite.set(0) 
 

            #=============Total Product Price and Tax variables==================== 
            self.cosmetic_price.set("") 
            self.grocery_price.set("") 
            self.cold_drink_price.set("") 
            self.cosmetic_tax.set("") 
            self.grocery_tax.set("") 
            self.cold_drink_tax.set("") 
 

            #=============Customer Detail================ 
            self.c_name.set("") 
            self.c_phon.set("") 
            self.bill_no.set("") 
            x=random.randint(1000,9999) 
            self.bill_no.set(str(x)) 
            self.search_bill.set("") 
            self.welcome_bill() 
    def Exit_app(self): 
        op=messagebox.askyesno("Exit","Do you want to exit?") 
        if op>0: 
            self.root.destroy() 

root=Tk() 
obj=Bill_App(root) 
root.mainloop()
