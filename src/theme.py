import tkinter as tk

greens = ['#66ff00', '#8bff4f','#a9ff77','#c2ff9b','#d8ffbd','#ecffde','#ffffff',]
#from green to white
theme_content = {
    ".": {
        "configure": {
            "background": '#ecffde' # All colors except for active tab-button
        }
    },
    "TButton": {
        "configure": {
            "background": '#a9ff77', # Color of non selected tab-button
            "borderwidth": 1,
            "bordercolor": "#66ff00",
            "padding": 5,
            "relief": tk.SOLID
        },
        "map": {
            "background": [("active", '#66ff00')] # Color of active tab
        }
    },
    "TNotebook": {
        "configure": {
            "background":'#ecffde' # color behind the notebook
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#ecffde', # Color of non selected tab-button
            "padding": [5, 2], # [space beetwen text and horizontal tab-button border, space between text and vertical tab_button border]
        },
        "map": {
            "background": [("selected", '#c2ff9b')], # Color of active tab
            "expand": [("selected", [10, 10, 10, 0])] # [expanse of text]
        }
    }
}

def theme():
    return theme_content
