    def bill_area(self): 
        if self.c_name.get()=="" or self.c_phon.get()=="": 
            messagebox.showerror("Error","Customer Details are Required") 
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0": 
            messagebox.showerror("Error","No Product Selected") 
        else: 
            self.welcome_bill() 



            #===cosmetics===== 
            if self.soap.get()!=0: 
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0: 
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}") 
            if self.face_wash.get()!=0: 
                self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}") 
            if self.spray.get()!=0: 
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_s_p}") 
            if self.gel.get()!=0: 
                self.textarea.insert(END,f"\n Hair Gel \t\t{self.gel.get()}\t\t{self.c_g_p}") 
            if self.lotion.get()!=0: 
                self.textarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_l_p}") 


                #===Grocery===== 
            if self.rice.get()!=0: 
                self.textarea.insert(END,f"\n Rice   \t\t{self.rice.get()}\t\t{self.g_r_p}") 
            if self.food_oil.get()!=0: 
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}") 
            if self.daal.get()!=0: 
                self.textarea.insert(END,f"\n Daal   \t\t{self.daal.get()}\t\t{self.g_d_p}") 
            if self.wheat.get()!=0: 
                self.textarea.insert(END,f"\n Wheat  \t\t{self.wheat.get()}\t\t{self.g_w_p}") 
            if self.sugar.get()!=0: 
                self.textarea.insert(END,f"\n Sugar  \t\t{self.sugar.get()}\t\t{self.g_s_p}") 
            if self.tea.get()!=0: 
                self.textarea.insert(END,f"\n Tea   \t\t{self.tea.get()}\t\t{self.g_t_p}") 


            #===Cold Drink===== 
            if self.maaza.get()!=0: 
                self.textarea.insert(END,f"\n Maaza   \t\t{self.maaza.get()}\t\t{self.cd_m_p}") 
            if self.coke.get()!=0: 
                self.textarea.insert(END,f"\n Coke   \t\t{self.coke.get()}\t\t{self.cd_c_p}") 
            if self.frooti.get()!=0: 
                self.textarea.insert(END,f"\n Frooti  \t\t{self.frooti.get()}\t\t{self.cd_f_p}") 
            if self.thumbsup.get()!=0: 
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.cd_th_p}") 
            if self.limca.get()!=0: 
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}") 
            if self.sprite.get()!=0: 
                self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t\t{self.cd_s_p}") 
            self.textarea.insert(END,f"\n--------------------------------------") 
            if self.cosmetic_tax.get()!="Rs. 0.0": 
                self.textarea.insert(END,f"\n Cosmetic Tax \t\t\t{self.cosmetic_tax.get()}") 
            if self.grocery_tax.get()!="Rs. 0.0": 
                self.textarea.insert(END,f"\n Grocery Tax \t\t\t{self.grocery_tax.get()}") 
            if self.cold_drink_tax.get()!="Rs. 0.0": 
                self.textarea.insert(END,f"\n ColdDrink Tax\t\t\t{self.cold_drink_tax.get()}") 
            self.textarea.insert(END,f"\n Total Bill  \t\t\t Rs. {self.total_bill}") 
            self.textarea.insert(END,f"\n---------------------------------------") 
        self.save_bill()
    
