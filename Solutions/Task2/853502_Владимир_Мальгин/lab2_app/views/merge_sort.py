from time import sleep
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
import threading

from lab2_merge_sort import merge_sort


class MergeSortView(Frame):
    def __init__(self, root, **kw):
        super().__init__(root, **kw)
        self.pack(fill="both", expand=1)
        configure_ttk_style()

        self.choose_input_file_button = ttk.Button(self, style="MergeSort.TButton", text="Open file to sort")
        self.choose_input_file_button.bind("<Button-1>", self.on_choose_input_file_button_click)
        self.choose_input_file_button.grid(row=0, column=0, padx=5, pady=5)
        self.input_file_label = Label(self, text="Input file: ")
        self.input_file_label.grid(row=0, column=1)
        self.input_file_name = StringVar()
        self.input_file_name.set("empty")
        self.input_file_name_label = Label(self, textvariable=self.input_file_name)
        self.input_file_name_label.grid(row=0, column=2)

        self.choose_output_file_button = ttk.Button(self, style="MergeSort.TButton",
                                                    text="Open file to save the result")
        self.choose_output_file_button.bind("<Button-1>", self.on_choose_output_file_button_click)
        self.output_file_label = Label(self, text="Output file: ")
        self.output_file_name = StringVar()
        self.output_file_name.set("empty")
        self.output_file_name_label = Label(self, textvariable=self.output_file_name)

        self.sort_button = ttk.Button(self, style="MergeSort.TButton",
                                      text="Sort!")
        self.sort_button.bind("<Button-1>", self.on_sort_click)

        self.processing_label_str = StringVar()
        self.processing_label = Label(self, textvariable=self.processing_label_str)
        self.is_sorting = False

    def on_choose_input_file_button_click(self, event):
        file_name = filedialog.Open(self, filetypes=[("*.txt files", ".txt")]).show()
        if file_name == '':
            return None
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        try:
            input_file = open(file_name)
            self.input_file_name.set(file_name)
            self.show_choose_output_button()
            input_file.close()
        except IOError as e:
            messagebox.showerror("Can't open this file\n", e)
            self.hide_choose_output_button()

    def on_choose_output_file_button_click(self, event):
        file_name = filedialog.SaveAs(self, filetypes=[("*.txt files", ".txt")]).show()
        if file_name == '':
            return None
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        try:
            output_file = open(file_name, 'w')
            self.output_file_name.set(file_name)
            self.show_sort_button()
            output_file.close()
        except IOError as e:
            messagebox.showerror("Can't open this file\n", e)
            self.hide_sort_button()

    def on_sort_click(self, event):
        self.is_sorting = True
        self.processing_label.grid(row=4, column=0)
        merge_sort(self.input_file_name.get(), self.output_file_name.get())
        messagebox.showinfo("Success!", "Sorting finished!")
        self.is_sorting = False

    def show_choose_output_button(self):
        self.choose_output_file_button.grid(row=1, column=0, padx=5, pady=5)
        self.output_file_label.grid(row=1, column=1)
        self.output_file_name_label.grid(row=1, column=2)

    def hide_choose_output_button(self):
        self.choose_output_file_button.grid_forget()
        self.output_file_label.grid_forget()
        self.output_file_name_label.grid_forget()

    def show_sort_button(self):
        self.sort_button.grid(row=2, column=0, pady=5)

    def hide_sort_button(self):
        self.sort_button.grid_forget()


def configure_ttk_style():
    ttk.Style().configure("MergeSort.TButton", padding=3, width=30, background="gray", relief="flat")
