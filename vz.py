import tkinter as tk


class Ventana(tk.Toplevel):
    def __init__(self, parent=None, **kwargs):
        super(Ventana, self).__init__(parent, **kwargs)
        self.overrideredirect(True)
        self.parent = parent
        self.X = 0
        self.Y = 0

        self.bt_x = tk.Button(
            self, text='X', command=self.cerrar, relief=tk.FLAT
        )
        cx, cy = self.winfo_x(), self.winfo_y()
        self.bt_x.place(x=2, y=2)
        self.bt_pin = tk.Button(self, text='M', command=self.mantener, relief=tk.FLAT)
        self.bt_pin.place(x=20, y=2)
        self.contenido = tk.Frame(self)
        self.contenido.pack(side=tk.TOP, fill=tk.BOTH)

        self.bind("<ButtonPress-1>", self.mueve_start)
        self.bind("<ButtonRelease-1>", self.mueve_stop)
        self.bind("<B1-Motion>", self.mueve)

        self.ONTOP = False

    def mueve_start(self, e):
        self.X, self.Y = e.x, e.y

    def mueve_stop(self, e):
        self.X, self.Y = None, None

    def mueve(self, e):
        dx, dy = (e.x - self.X), (e.y - self.Y)
        nueva_pos = f"+{self.winfo_x()+dx}+{self.winfo_y()+dy}"
        self.geometry(nueva_pos)
        self.parent.geometry(nueva_pos)

    def cerrar(self):
        self.parent.destroy()
        # self.parent.parent.destroy()

    def mantener(self):
        self.ONTOP = False if self.ONTOP else True
        self.attributes('-topmost', self.ONTOP)
        self.update()


class MiVentana(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(MiVentana, self).__init__(*args, **kwargs)
        self.resizable(0,0)
        self.geometry("0x0")
        self._titulo = tk.StringVar(self.titulo())

        self.vsb = Ventana(self)
        self.vsb.geometry("300x120")
        self.bind("<Map>", self.mt_deicon)
        self.bind("Unmap", self.mt_draw)

    def titulo(self, *args):
        if args:
            self._titulo.set(args[0])
        super(MiVentana, self).title(args)

    def mt_draw(self, e):
        self.vsb.withdraw()

    def mt_deicon(self, e):
        self.vsb.deiconify()

if __name__=="__main__":
    rz = MiVentana()
    rz.titulo("MI ventana")
    rz.mainloop()
