from tkinter import ttk


def create(root):
    style = ttk.Style(root)
    style.theme_use("winnative")
    style.configure("TopPanel.TFrame",
                    background="gray",
                    foreground="black")
    return style


if __name__ == '__main__':
    pass