import tkinter as tk
from tkinter import ttk

from interface import Pysum

_version_ = '1.2.2'

if __name__ == "__main__":
    print(f'Welcome to PYSUM v{_version_}!')

    title = 'PYSUM'
    pysum = Pysum(title)
