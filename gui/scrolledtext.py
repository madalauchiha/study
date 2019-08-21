#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from tkinter import *


class ScrollText(Frame):
    def __init__(self, path_file, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets(path_file)

    def make_widgets(self, path_file):
        sbar = Scrollbar(self)
        text = Text(self)

        sbar.config(command=text.yview, relief=SUNKEN)
        text.config(yscrollcommand=sbar.set)

        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)

        chars = open(path_file, 'r').read()
        text.delete('1.0', END)
        text.insert('1.0', chars)
        text.mark_set(INSERT, '1.0')
        text.focus()

        self.text = text

    def get_text(self):
        return self.text.get('1.0', END+'-2c')


if __name__ == '__main__':
    path_file = '/home/dingding/Work/GG/GG2.6/auto/gg2.6_auto_v0.6/configs/config.ini'
    st = ScrollText(path_file)
    print(repr(st.get_text()))
    st.mainloop()
