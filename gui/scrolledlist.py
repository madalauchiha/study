#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from tkinter import *


class ScrollList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets(options)

    def run_cmd(self, label):
        print(label)

    def handle_list(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.run_cmd(label)

    def make_widgets(self, options):
        sbar = Scrollbar(self)
        lbox = Listbox(self)

        sbar.config(command=lbox.yview, relief=SUNKEN)
        lbox.config(yscrollcommand=sbar.set)

        sbar.pack(side=RIGHT, fill=Y)
        lbox.pack(side=LEFT, expand=YES, fill=BOTH)

        row = 0
        for label in options:
            lbox.insert(row, label)
            row += 1

        lbox.bind('<Double-1>', self.handle_list)

        self.listbox = lbox


def test_name():
    print(__name__)


if __name__ == '__main__':
    options = (('option %d' % i) for i in range(20))
    ScrollList(options).mainloop()
