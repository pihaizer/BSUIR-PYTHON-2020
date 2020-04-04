from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from lab2_vector import Vector


class VectorView(Frame):
    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        self.pack(fill="both", expand=1)

        Grid.columnconfigure(self, [0, 2], weight=1)
        Grid.rowconfigure(self, 1, weight=1)

        input_label = Label(self, text="Input")
        self.input_field = Text(self, width=30, height=20, relief="ridge", borderwidth=2)
        input_label.grid(row=0, column=0, sticky=N)
        self.input_field.grid(row=1, column=0, sticky=N + E + S + W)

        process_btn = Button(self, width=10, text="Process",
                             relief="ridge", borderwidth=2)
        process_btn.bind("<Button-1>", self.process_input)
        process_btn.grid(row=0, column=1, rowspan=2, padx=5)

        output_label = Label(self, text="Output")
        self.output_field = Text(self, width=30, height=20, relief="ridge", borderwidth=2)
        output_label.grid(row=0, column=2, sticky=N)
        self.output_field.grid(row=1, column=2, sticky=N + E + S + W)

    def process_input(self, event):
        try:
            self.output_field.delete(1.0, END)
            for line in str(self.input_field.get(1.0, END)).splitlines():
                output = ""
                exec(line)
                try:
                    output = eval(line)
                except Exception:
                    pass
                self.output_field.insert(1.0, output)
        except Exception as e:
            messagebox.showerror("Invalid input", e)
