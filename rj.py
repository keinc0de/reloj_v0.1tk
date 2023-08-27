import tkinter as tk
from vz import MiVentana

class RelojTk(MiVentana):
    def __init__(self):
        super(RelojTk, self).__init__()



if __name__=="__main__":
    app = RelojTk()
    app.mainloop()