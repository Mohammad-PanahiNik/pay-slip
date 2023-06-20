import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.button1 = tk.Button(self, text="Page 1", command=self.open_page1)
        self.button2 = tk.Button(self, text="Page 2", command=self.open_page2)
        self.button1.pack()
        self.button2.pack()

    def open_page1(self):
        self.master.switch_frame(Page1)

    def open_page2(self):
        self.master.switch_frame(Page2)


class Page1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text="This is Page 1")
        self.label.pack()
        self.back_button = tk.Button(self, text="Back to Main", command=self.go_back)
        self.back_button.pack()

    def go_back(self):
        self.master.switch_frame(MainPage)


class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text="This is Page 2")
        self.label.pack()
        self.back_button = tk.Button(self, text="Back to Main", command=self.go_back)
        self.back_button.pack()

    def go_back(self):
        self.master.switch_frame(MainPage)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Page Layout Example")
        self.geometry("400x300")
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
