from tkinter import *
from tkinter import ttk

import lab2_json as json


class JsonView(Frame):
    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        self.pack(fill="both", expand=1)

        Grid.columnconfigure(self, [0, 2], weight=1)
        Grid.rowconfigure(self, 2, weight=1)

        self.switcher_var = StringVar(self)
        self.switcher_options = ["Serialize", "Deserialize"]
        self.switcher = ttk.OptionMenu(self, self.switcher_var,
                                       self.switcher_options[0],
                                       *self.switcher_options)
        self.switcher.configure(width=30)
        self.switcher.grid(row=0, column=0, columnspan=3, sticky=N)

        self.input_label = Label(self, text="Input")
        self.input_field = Text(self, width=30, height=20, relief="ridge", borderwidth=2)
        self.input_label.grid(row=1, column=0, sticky=N)
        self.input_field.grid(row=2, column=0, sticky=N+E+S+W)

        self.process_btn = Button(self, width=10, textvariable=self.switcher_var,
                                  relief="ridge", borderwidth=2)
        self.process_btn.bind("<Button-1>", self.process_input)
        self.process_btn.grid(row=1, column=1, rowspan=2, padx=5)

        self.output_label = Label(self, text="Output")
        self.output_field = Text(self, width=30, height=20, relief="ridge", borderwidth=2)
        self.output_label.grid(row=1, column=2, sticky=N)
        self.output_field.grid(row=2, column=2, sticky=N+E+S+W)

    def process_input(self, event):
        self.output_field.delete(1.0, END)
        if self.switcher_var.get() == self.switcher_options[0]:
            obj = eval(self.input_field.get(1.0, END))
            self.output_field.insert(1.0, json.serialize_pretty(obj))
        elif self.switcher_var.get() == self.switcher_options[1]:
            serialized = json.deserialize(self.input_field.get(1.0, END))
            self.output_field.insert(1.0, str(serialized))
