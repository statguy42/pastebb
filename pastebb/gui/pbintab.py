import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class PastebinTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pbin_tabs = ttk.Notebook(self)
        self.newpaste_tab = NewPasteTab(self.pbin_tabs)
        self.history_tab = ttk.Frame(self.pbin_tabs)
        self.pbin_tabs.add(self.newpaste_tab, text = "Create new paste")
        self.pbin_tabs.add(self.history_tab, text = "History")
        self.pbin_tabs.pack(expand = 1, fill = "both")


class NewPasteTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.source_frame = ttk.Frame(self)
        self.paste_button = ttk.Button(self.source_frame, text = "Paste from clipboard")
        self.paste_button.grid(row = 0, column = 0)
        self.open_file_button = ttk.Button(self.source_frame, text = "Open text file")
        self.open_file_button.grid(row = 0, column = 1)
        self.source_frame.pack()

        self.textarea = ScrolledText(self)
        self.textarea.pack()

        self.paste_options_frame = PasteOptionsFrame(self)
        self.paste_options_frame.pack()

        self.output_frame = PasteOutputFrame(self)
        self.output_frame.pack()


class PasteOptionsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.placeholder = ttk.Label(self, text = "options here")
        self.placeholder.grid(row = 0, column = 0)

        self.submit_button = ttk.Button(self, text = "Submit")
        self.submit_button.grid(row = 4, column = 0, columnspan = 2)


class PasteOutputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.error_status = 1
        # will be set to 0 on a successful paste

        self.link_label = ttk.Label(self, text = "Paste link:")
        self.link_label.grid(row = 0, column = 0)

        self.link_var = tk.StringVar()
        self.link_entry = ttk.Entry(self, textvariable = self.link_var, state = tk.DISABLED)
        self.link_entry.grid(row = 0, column = 1)

        self.copy_link_button = ttk.Button(self, text = "Copy link", command = lambda: self.copy_link(self.link_var.get()))
        self.copy_link_button.grid(row = 0, column = 2)

    def copy_link(self, link):
        if self.error_status == 0:
            # only if no error occured
            self.clipboard_clear()
            self.clipboard_append(link)
