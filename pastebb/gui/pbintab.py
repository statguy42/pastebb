import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename

class PastebinTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pbin_tabs = ttk.Notebook(self)
        self.newpaste_tab = NewPasteTab(self.pbin_tabs)
        self.history_tab = ttk.Frame(self.pbin_tabs)    # TODO
        self.pbin_tabs.add(self.newpaste_tab, text = "Create new paste")
        self.pbin_tabs.add(self.history_tab, text = "History")
        self.pbin_tabs.pack(expand = 1, fill = "both")


class NewPasteTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.source_frame = ttk.Frame(self)
        self.paste_button = ttk.Button(self.source_frame, text = "Paste from clipboard", command = self.paste_clipboard)
        self.paste_button.grid(row = 0, column = 0)
        self.open_file_button = ttk.Button(self.source_frame, text = "Open text file", command = self.get_text_from_file)
        self.open_file_button.grid(row = 0, column = 1)
        self.source_frame.pack()

        self.textarea = ScrolledText(self)
        self.textarea.pack()

        self.paste_options_frame = PasteOptionsFrame(self)
        self.paste_options_frame.pack()

        self.output_frame = PasteOutputFrame(self)
        self.output_frame.pack()

    def paste_clipboard(self):
        # TODO: add error handling
        self.textarea.delete("1.0", "end")
        self.textarea.insert("end", self.clipboard_get())

    def get_text_from_file(self):
        filename = askopenfilename(parent = self, title = "Select file to open")
        # TODO: set allowed filetypes
        # TODO: add error handling
        with open(filename) as f:
            self.textarea.delete("1.0", "end")
            self.textarea.insert("end", f.read())


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

        self.link_var = tk.StringVar()    # stringvar to hold the pastebin link
        self.link_entry = ttk.Entry(self, textvariable = self.link_var, state = tk.DISABLED)    # DISABLED so that user cannot change it
        self.link_entry.grid(row = 0, column = 1)

        self.copy_link_button = ttk.Button(self, text = "Copy link", command = lambda: self.copy_link(self.link_var.get()))
        self.copy_link_button.grid(row = 0, column = 2)

    def copy_link(self, link):
        if self.error_status == 0:
            # only if no error occured
            self.clipboard_clear()
            self.clipboard_append(link)
