import tkinter as tk

class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_url = tk.Label(self, text="URL")
        self.label_port = tk.Label(self, text="Port")
        self.label_register = tk.Label(self, text="Register")
        self.label_value = tk.Label(self, text="Value")

        self.entry_url = tk.Entry(self)
        self.entry_port = tk.Entry(self)
        self.entry_register = tk.Entry(self)
        self.entry_value = tk.Entry(self)
        self.status= tk.Label(self)

        self.label_url.grid(row=0, sticky=tk.E)
        self.label_port.grid(row=1, sticky=tk.E)
        self.label_register.grid(row=2, sticky=tk.E)
        self.label_value.grid(row=3, sticky=tk.E)

        self.entry_url.grid(row=0, column=1, padx=5, pady=5)
        self.entry_port.grid(row=1, column=1, padx=5, pady=5)
        self.entry_register.grid(row=2, column=1, padx=5, pady=5)
        self.entry_value.grid(row=3, column=1, padx=5, pady=5)
        self.status.grid(row=4, columnspan=2, sticky = tk.W + tk.E)

        self.btn_send = tk.Button(self, text="Send", command=self.some_command, font=("Ubuntu", 10), bg="#fab90f", fg="black")
        self.btn_send.grid(columnspan=2)

        self.pack()

    def some_command():
        pass


root = tk.Tk()
lf = MainScreen(root)
root.title("Modbus TCP/IP Tester")
root.resizable(False, False)
root.mainloop()
