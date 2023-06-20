from tkinter import *

class MainPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.main_menu()

    def main_menu(self):
        self.configure(bg='#191818')
        self.addListBtnImg = PhotoImage(file='images/list_img.png')
        self.addPersonnelImg = PhotoImage(file='images/add_personell_img.png')
        self.payroll_img = PhotoImage(file='images/payroll_img.png')
        
        header_menu_lbl = LabelFrame(width=1200,height=80,bg='#BEC8CF',bd=5,relief='solid')
        header_menu_txt = Label(text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        
        self.btn_list = Button(width=400,height=620,image=self.addListBtnImg,bd=0,cursor='hand2',activebackground='#191818',command=self.open_receipt)
        self.btn_add_personnel = Button(width=400,height=620,image=self.addPersonnelImg,bd=0,cursor='hand2',activebackground='#191818')
        self.btn_payroll = Button(width=400,height=620,image=self.payroll_img,bd=0,cursor='hand2',activebackground='#191818')
        
        
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        self.btn_list.place(x=0,y=80)
        self.btn_add_personnel.place(x=400,y=80)
        self.btn_payroll.place(x=800,y=80)

    def open_receipt(self):
        self.master.switch_frame(receipt)
        
class receipt(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        header_menu_lbl = LabelFrame(width=1200,height=80,bg='red',bd=5,relief='solid')
        header_menu_txt = Label(text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        header_menu_txt.place(x=510,y=15)
        header_menu_lbl.place(x=0,y=0)
        
    
        
        
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("payroll")
        self.geometry("1200x700+320+150")
        self.iconbitmap('payroll-icon.ico')
        self.current_frame = None
        self.switch_frame(MainPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()