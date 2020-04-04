import tempfile
from tkinter import *
from tkinter import ttk
from typing import TextIO

import lab2_app.style as style
from lab2_app.views import *

opened_file: TextIO
save_file: TextIO


def main():
    root = Tk()
    style.create(root)
    root.title("Lab 2")

    tabs = ttk.Notebook(root)
    tabs.add(JsonView(root), text="Json")
    tabs.add(VectorView(root), text="Vector")
    tabs.add(MergeSortView(root), text="Merge sort")
    tabs.pack(expand=1, fill="both")

    root.mainloop()


if __name__ == '__main__':
    main()
