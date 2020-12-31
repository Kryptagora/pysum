import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np

from src.theme import theme
from src.algorithm import blosum

def qopen(path:str):
    '''Opens and returns file content'''
    with open(path, 'r') as fh:
        content = fh.read()
    return content


class Pysum(tk.Frame):
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.configure(background='#ecffde')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.style = ttk.Style()
        self.style.theme_create('bio', settings=theme())
        self.style.theme_use('bio')

        self.font_1 = ('consolas', 10, 'bold')
        self.font_2 = ('consolas', 10)
        self.main_text = qopen('src/main_texts.txt').split('\n\n')

        self.tabs = ttk.Notebook(self.root, padding=10)
        self.result_frame = None

        self.add_tabs()
        self.add_content_tool()

        self.matrix_labels = None
        self.matrix_result = None

        self.root.mainloop()


    def add_tabs(self):
        self.tool = ttk.Frame(self.tabs)
        self.tabs.add(self.tool, text=' Tool ')

        self.results = ttk.Frame(self.tabs)
        self.tabs.add(self.results, text=' Results ')

        self.settings = ttk.Frame(self.tabs)
        self.tabs.add(self.settings, text=' Settings ')

        self.about = ttk.Frame(self.tabs)
        self.tabs.add(self.about, text=' About ')

        self.tabs.grid(row=0, column=0)

    def add_content_tool(self):
        tool_frame = ttk.LabelFrame(self.tool, text="File Structure", padding=50, relief=tk.RIDGE)

        tool_frame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        tf_l1 = ttk.Label(tool_frame, text=self.main_text[0], font=self.font_1)
        tf_l1.grid(row=0, column=0, pady=3, columnspan=3, sticky="w")

        tf_l2 = ttk.Label(tool_frame, text=self.main_text[1], font=self.font_2)
        tf_l2.grid(row=1, column=0, pady=3, columnspan=3, sticky="w")

        tf_l3 = ttk.Label(tool_frame, text=self.main_text[2], font=self.font_1)
        tf_l3.grid(row=2, column=0, pady=3, columnspan=3, sticky="w")

        tf_l3 = ttk.Label(tool_frame, text=self.main_text[3], font=self.font_2)
        tf_l3.grid(row=3, column=0, pady=3, columnspan=3, sticky="w")

        # ---
        in_frame = ttk.LabelFrame(self.tool, text="Input", padding=50, relief=tk.RIDGE)
        in_frame.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        self.tf_textin = tk.Text(in_frame, height=6, width=50)
        self.tf_textin.grid(row=1, column=0, columnspan=1, sticky="w")
        self.tf_textin.insert(tk.END, self.main_text[4])

        tf_open_text = ttk.Button(in_frame, text="Open File", command=self.tf_open_file)
        tf_open_text.grid(row=1, column=1, sticky="news")

        tf_clear_text = ttk.Button(in_frame, text="Clear Input", command=lambda: self.tf_textin.delete(1.0, tk.END))
        tf_clear_text.grid(row=1, column=2, sticky="news")

        tf_l4 = ttk.Label(in_frame, text=self.main_text[5], font=self.font_1)
        tf_l4.grid(row=2, column=0, pady=5, columnspan=1, sticky="w")

        self.xx_textin = tk.Text(in_frame, height=1, width=9)
        self.xx_textin.grid(row=2, column=1, columnspan=1, sticky="w")
        self.xx_textin.insert(tk.END, '')

        tf_start_calc = ttk.Button(in_frame, text="CALCULATE!", command=self.check_input_and_pass)
        tf_start_calc.grid(row=2, column=2, sticky="news")


    def add_content_result(self):
        assert self.matrix_result is not None
        if self.result_frame is not None:
            #dynamicly resize window
            self.result_frame.destroy()

        self.result_frame = ttk.LabelFrame(self.results, text="Matrix Representation", padding=50, relief=tk.RIDGE)
        self.result_frame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        for (row, col), value in np.ndenumerate(self.matrix_result):
            if row == 0:
                ttk.Label(self.result_frame, text=str(self.matrix_labels[col]), font=self.font_1).grid(row=row, column=col+1)

            if col == 0:
                ttk.Label(self.result_frame, text=str(self.matrix_labels[row]), font=self.font_1).grid(row=row+1, column=col)

            _ = ttk.Entry(self.result_frame, width=10, font=self.font_2)
            _.insert(tk.END, str(value))
            _.grid(row=row+1, column=col+1)
            _.configure(state="readonly")

        # ---
        out_res_frame = ttk.LabelFrame(self.results, text="Matrix Representation", padding=50, relief=tk.RIDGE)
        out_res_frame.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S)
        #TODO
        # print to console
        # print to file
        # export as csv (maybe)



    def tf_open_file(self):
        tf_filename = filedialog.askopenfilename(initialdir="/home/amon/Desktop", title="Select Text File", filetypes=
            (("txt files", "*.txt"), ("all files", "*.*")))
        if len(tf_filename) == 0:
            return False
        with open(tf_filename, 'r') as fh:
            tf_text = fh.read()

        self.tf_textin.delete("1.0", tk.END)
        #self.tf_textin.insert(tk.END, tf_text)
        self.tf_textin.insert(tk.END, f'--File sucessfully loaded: {len(tf_text.splitlines())} sequences found.--\n'+tf_text)

    def check_input_and_pass(self):
        dna_sequences = []
        initial_len = None
        xx_number = self.xx_textin.get("1.0", "end-1c").rstrip()
        # first check xx_blosum value
        try:
            xx_number = int(xx_number)
            if not xx_number in range(0, 101):
                self.warn(mode='xnumrange')
                return False
        except:
            self.warn(mode='xnuminvalid')
            return False

        seq_string = self.tf_textin.get("1.0", tk.END).rstrip()
        if len(seq_string.splitlines()) < 2:
            self.warn(mode='empty')
            return False

        for i, line in enumerate(seq_string.upper().splitlines()):
            if line.startswith('-'):
                continue

            if initial_len is None:
                initial_len = len(line)

            if initial_len != len(line):
                self.warn(mode='len', line=i)
                return False
            else:
                dna_sequences.append(line)

        try:
            self.matrix_result, self.matrix_labels = blosum(dna_sequences, xx_number)
        except:
            self.warn(mode='something', line=i)
            return False

        self.add_content_result()
        self.tabs.select([1])
        print(self.matrix_result)

    def warn(self, mode:str, line:int=0):
        warn_msg = tk.StringVar()
        if mode == 'len':
            warn_msg.set(f'[WARNING] Sequence nr.{line+1} differs in lenght!')
        elif mode == 'empty':
            warn_msg.set(f'[WARNING] At least 2 Sequences must be given!')
        elif mode == 'xnumrange':
            warn_msg.set(f'[WARNING] BLOSUM Degree must be between 1-100!')
        elif mode == 'xnuminvalid':
            warn_msg.set(f'[WARNING] BLOSUM Degree must be a number!')
        elif mode == 'something':
            warn_msg.set(f'[WARNING] BLOSUM cant be computed with that sequences!')
        else:
            warn_msg.set(f'[WARNING] This will never happen.')

        warning_label = tk.Label(self.tool, textvariable=warn_msg, font=self.font_1, fg="red", bg='#ecffde')
        warning_label.grid(row=2, column=0, pady=5, sticky="w")
        self.root.after(4000, lambda: warn_msg.set(""))
