# pip install pyqt5-tools
# C:\Users\kobto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\pyqt5_tools\Qt\bin - путь к дизайнеру

from tkinter import *
import time
import threading


class But_print():
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "to count"
        self.but.bind("<Button-1>", self.printer)
        self.but.pack()

    def thread(func):
        '''
        Это простейший декоратор. В него мы будем заворачивать 
        функции. Любая функция, завернутая этим декоратором, 
        будет выполнена в отдельном потоке.
        '''
        def wrapper(*args, **kwargs):
            current_thread = threading.Thread(
                target=func, args=args, kwargs=kwargs)
            current_thread.start()

        return wrapper

    @thread  # собственно, применяем декоратор
    def printer(self, event):
        for i in range(10):
            print(10 - i - 1, "second")
            time.sleep(1)


root = Tk()
obj = But_print()
root.mainloop()
