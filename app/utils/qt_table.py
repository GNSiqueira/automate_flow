from qt_core import *

def expanding_header_table(table, locate, expanding: bool = None): 
    if expanding == True: 
        table.horizontalHeader().setSectionResizeMode(locate, QHeaderView.Stretch)
    elif expanding == False: 
        table.horizontalHeader().setSectionResizeMode(locate, QHeaderView.ResizeToContents) 
    else: 
        pass