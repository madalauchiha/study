#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue, Empty
from tkinter.scrolledtext import ScrolledText
from time import sleep


class ThreadGui(ScrolledText):
    def __init__(self, parent=None):
        self.data_queue = Queue()

        ScrolledText.__init__(self, parent)
        self.pack()

        self.bind('<Button-1>', self.make_threads)
        self.consumer()

    def producer(self, id):
        for i in range(5):
            sleep(5)
            print('put => thread %d producer %d' % (id, i))
            self.data_queue.put('thread %d producer %d' % (id, i))

    def make_threads(self, event):
        for i in range(4):
            Thread(target=self.producer, args=(i,)).start()

    def consumer(self):
        try:
            data = self.data_queue.get(block=False)
            print('get => ' + str(data))
        except Empty:
            pass
        else:
            self.insert('end', str(data)+'\n')
            self.see('end')

        self.after(250, self.consumer)


if '__main__' == __name__:
    ThreadGui().mainloop()
