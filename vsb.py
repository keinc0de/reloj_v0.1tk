import tkinter as tk
import time
import pyglet


class MiVentana(tk.Tk):
    def __init__(self, wv=130, hv=40, **kwargs):
        super().__init__(**kwargs)
        self.wv, self.hv = wv, hv
        self._config_mv()

    def _config_mv(self):
        fg0 = "white"
        bg = "#140D1B"
        self.fg1 = "#515D57"
        self.fg2 = "#1D8B4F"
        self.ONTOP = False
        self.config(bd=1, bg="#303030")
        self.geometry(f"{self.wv}x{self.hv}")
        self.overrideredirect(True)

        self.titulo = tk.Label(self, text=" mi titulo", bg=bg, fg=fg0)
        self.titulo.place(x=2, y=2)
        self.bind("<B1-Motion>", self.mueve_ventana)
        pyglet.options['win32_gdi_font'] = True
        pyglet.font.add_file('Handjet-Regular.ttf')
        self.lb_tiempo = tk.Label(self, bg=bg, fg=fg0, font=('Handjet', 25))
        self.lb_tiempo.pack(expand=1, fill='both')

        # self.btx = tk.Button(self, text="X", command=self.quit, relief='flat',bg=bg, fg=fg0)
        # self.btx.place(x=self.wv-20, y=2)

        self.lbx = tk.Label(self, text="X", bg=bg, fg=self.fg1)
        self.lbx.place(x=self.wv-16, y=1)
        self.lbx.bind("<Button-1>", self.cerrar)
        self.lbm = tk.Label(self, text="M", bg=bg, fg=self.fg1)
        self.lbm.place(x=self.wv-19, y=16)
        self.lbm.bind("<Button-1>", self.mantener)

        self.muestra_tiempo()

    def mueve_ventana(self, e):
        self.geometry(f"+{e.x_root}+{e.y_root}")

    def obten_tiempo(self):
        return time.strftime("%H:%M:%S")
    
    def muestra_tiempo(self):
        self.lb_tiempo.config(text=self.obten_tiempo())
        self.lb_tiempo.after(1000, self.muestra_tiempo)
    
    def cerrar(self, e):
        self.quit()

    def mantener(self, e):
        self.ONTOP = False if self.ONTOP else True
        fg = self.fg2 if self.ONTOP else self.fg1
        self.lbm.config(fg=fg)
        self.attributes('-topmost', self.ONTOP)
        self.update()


if __name__=="__main__":
    app = MiVentana()
    app.mainloop()