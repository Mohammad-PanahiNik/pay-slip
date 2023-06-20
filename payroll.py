from tkinter import *

class MainPage(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.main_menu()

    def main_menu(self):
        self.addListBtnImg = PhotoImage(file='images/list.png')
        self.addPersonnelImg = PhotoImage(file='images/register.png')
        self.paySlipImg = PhotoImage(file='images/payroll.png')
        btn_color='#BBBBBB'
        self.y=250
        
        header_menu_lbl = LabelFrame(width=1200,height=80,bg='#BEC8CF',bd=5,relief='solid')
        header_menu_txt = Label(text='PAYROLL',font=('B Titr',23,'bold'),bg='#BEC8CF')
        self.frm_list = LabelFrame(width=400,height=620,bg=btn_color,bd=5,relief='solid',cursor='hand2')
        img_list = Label(width=150,height=150,image=self.addListBtnImg,bg=btn_color)
        txt_list = Label(text='لیست کارکنان',font=('B Titr',23,'bold'),bg=btn_color)
        self.frm_add_personnel = LabelFrame(width=400,height=620,bg=btn_color,bd=5,relief='solid',cursor='hand2')
        img_add_personnel = Label(width=150,height=150,image=self.addPersonnelImg,bg=btn_color)
        txt_add_personnel = Label(text='ثبت کارمند جدید',font=('B Titr',23,'bold'),bg=btn_color)
        self.frm_pay_slip = LabelFrame(width=400,height=620,bg=btn_color,bd=5,relief='solid',cursor='hand2')
        img_pay_slip = Label(width=150,height=150,image=self.paySlipImg,bg=btn_color)
        txt_pay_slip = Label(text='ثبت کارمند جدید',font=('B Titr',23,'bold'),bg=btn_color)
        
        # self.frm_list.bind('<ENTER>',self.h_btn_menu)
        
        header_menu_txt.place(x=530,y=15)
        header_menu_lbl.place(x=0,y=0)
        self.frm_list.place(x=0,y=80)
        img_list.place(x=125,y=250)
        txt_list.place(x=110,y=400)
        self.frm_add_personnel.place(x=400,y=80)
        img_add_personnel.place(x=525,y=250)
        txt_add_personnel.place(x=510,y=400)
        self.frm_pay_slip.place(x=800,y=80)
        img_pay_slip.place(x=925,y=250)
        txt_pay_slip.place(x=910,y=400)

    
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