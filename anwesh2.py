    def total(self): 
        self.c_s_p=self.soap.get()*40 
        self.c_fc_p=self.face_cream.get()*120 
        self.c_fw_p=self.face_wash.get()*60 
        self.c_spr_p=self.spray.get()*180 
        self.c_g_p=self.gel.get()*140 
        self.c_l_p=self.lotion.get()*180 
        self.total_cosmetic_price=float( 
                                    self.c_s_p+ 
                                    self.c_fc_p+ 
                                    self.c_fw_p+ 
                                    self.c_spr_p+ 
                                    self.c_g_p+ 
                                    self.c_l_p 
                                  ) 
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price)) 
        self.c_tax=round(self.total_cosmetic_price*0.05,2) 
        self.cosmetic_tax.set("Rs. "+str(self.c_tax)) 
        self.g_r_p=self.rice.get()*80 
        self.g_fo_p=self.food_oil.get()*180 
        self.g_w_p=self.wheat.get()*60 
        self.g_d_p=self.daal.get()*240 
        self.g_s_p=self.sugar.get()*45 
        self.g_t_p=self.tea.get()*150 
        self.total_grocery_price=float( 
                                    self.g_r_p+ 
                                    self.g_fo_p+ 
                                    self.g_w_p+ 
                                    self.g_d_p+ 
                                    self.g_s_p+ 
                                    self.g_t_p 
                                  ) 
        self.grocery_price.set("Rs. "+str(self.total_grocery_price)) 
        self.g_tax=round(self.total_grocery_price*0.1,2) 
        self.grocery_tax.set("Rs. "+str(self.g_tax)) 
        self.cd_m_p=self.maaza.get()*60 
        self.cd_c_p=self.coke.get()*60 
        self.cd_f_p=self.frooti.get()*50 
        self.cd_th_p=self.thumbsup.get()*45 
        self.cd_l_p=self.limca.get()*40 
        self.cd_s_p=self.sprite.get()*60 
        self.total_cold_drink_price=float( 
                                    self.cd_m_p+ 
                                    self.cd_c_p+ 
                                    self.cd_f_p+ 
                                    self.cd_th_p+ 
                                    self.cd_l_p+ 
                                    self.cd_s_p 
                                   ) 
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price)) 
        self.cd_tax=round(self.total_cold_drink_price*0.05,2) 
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax)) 
        self.total_bill=float( 
            self.total_cosmetic_price+ 
            self.total_grocery_price+ 
            self.total_cold_drink_price+ 
            self.c_tax+ 
            self.g_tax+ 
            self.cd_tax 
        ) 
   
    def welcome_bill(self): 
        self.textarea.delete('1.0',END) 
        self.textarea.insert(END,"\t Welcome to Krishna Retails")  
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}") 
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}") 
        self.textarea.insert(END,f"\n======================================") 
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice") 
        self.textarea.insert(END,f"\n======================================") 
    
