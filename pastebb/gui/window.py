import tkinter as tk
from tkinter import ttk
from gui.pbintab import PastebinTab

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PasteBB")

        self.tabs = ttk.Notebook(self)
        self.pbin_tab = PastebinTab(self.tabs)
        self.imgbb_tab = ttk.Frame(self.tabs)
        self.tabs.add(self.pbin_tab, text = "Pastebin")
        self.tabs.add(self.imgbb_tab, text = "ImgBB")
        self.tabs.pack(expand = 1, fill = "both")

        self.status_bar_label = ttk.Label(self, text = "Ready", relief="sunken", anchor="w")
        self.status_bar_label.pack(side="bottom", fill="x")