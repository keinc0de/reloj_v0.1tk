import tkinter as tk
import time
import pyglet
import locale
from datetime import datetime


class MiReloj(tk.Tk):
    def __init__(self, wv=100, hv=40, **kwargs):
        super().__init__(**kwargs)
        self.ANCHO, self.ALTO = wv, hv
        self._config_mr()

    def _config_mr(self):
        self.icos = {
            'x':'''iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAgUlEQVR4nJ2R3QmAMAyEP38GK
            3SFTlF8cBTB4hSuIDiXL/qShCAK1oNCk7sLzRX+IqZwxBTyQz/HFA6tWxUDHVC8Se4z0KmpF24UAjGpZ
            wYap7HCT7Oew7Ct+8KdFFNx/dOLbYcaVD+pfREPck6pLT1NqTjSpklamt4E2C6fP64aF8TTM+w2d/2SA
            AAAAElFTkSuQmCC''',
            'lc':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAcElEQVR4nGNgGGjAiE1w8fyJ
            /7GJxybmY6hnwqV5+fK7W2MT8xljE/MZly+/uxWXwRgGwDRv2zXJB8bftmuSD8wQogwgBVBsAEqg4Ao8
            dIAcmHhdAAtEfGrwGkCMiwi6gCIDiAEUG8CCT5LYWBlYAAA+jiljF2m/rwAAAABJRU5ErkJggg==''',
            'la':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAf0lEQVR4nGNgoBAwYhNcPH/i
            f2zisYn5GOoxBBbPn/h/+fK7WxkYGBi27Zrkw8DAwODllrclMlLZG5shTLicBtMMY8MMRQc4DSAWsKAL
            YPMnPkCxCyg2AMW5uKIPHSB7E68LYhPzGQmFCV4DiHERQRdQZAAxgPoJCRkQGysUAQArRiX21611qwAA
            AABJRU5ErkJggg=='''
        }
        bg = '#101010'
        fg = '#D8D2C0'
        fgd = '#9AA698'
        fo = ('Consolas', 8, 'bold')
        self.OP = 1
        self.ON_TOP = True
        
        self.geometry(f"{self.ANCHO}x{self.ALTO}+400+200")
        self.overrideredirect(True)
        self.bind('<B1-Motion>', self.mover_ventana)
        self.config(bg=bg)

        self.cv = tk.Canvas(
            self, width=self.ANCHO, height=self.ALTO, bg=bg,
            highlightthickness=0
        )
        self.cv.pack(fill='both', expand=True)

        self.img_x = tk.PhotoImage(data=self.icos.get('x'))
        self.ix = self.cv.create_image(self.ANCHO-10, 8, image=self.img_x)
        self.cv.tag_bind(self.ix, '<Button-1>', self.cerrar)
        locale.setlocale(locale.LC_ALL, '')
        dia = datetime.today().strftime('%a %d')
        self.SD = self.cv.create_text(
            24, 8, text=dia.upper(), fill=fg, font=fo,
            justify='left'
        )

        pyglet.options['win32_gdi_font'] = True
        pyglet.font.add_file('BlackOpsOne-Regular.ttf')
        fot = ('Black Ops One', 18)
        self.TM = self.cv.create_text(
            42, 24,
            fill=fg, font=fot, text='22:45'
        )
        self.SG = self.cv.create_text(
            66, 6, text='00', fill=fgd, font=('Black Ops One', 12),
            justify='left'
        )

        self.img_lc = tk.PhotoImage(data=self.icos.get('lc'))
        self.ilc = self.cv.create_image(self.ANCHO-10, 28, image=self.img_lc)
        self.cv.tag_bind(self.ilc, '<Button-1>', self.mantener)

        self.bind('<KeyPress-Left>', self.izq)
        self.bind('<KeyPress-Right>', self.der)
        self.bind('<space>', self.normal)
        self.bind('<Alt-x>', self.cerrar)
        self.muestra_tiempo()
        self.mantener()

    def cerrar(self, e):
        self.quit()

    def mover_ventana(self, e):
        self.geometry(f"+{e.x_root}+{e.y_root}")
    
    def mantener(self, e=None):
        img = self.icos.get('lc') if self.ON_TOP else self.icos.get('la')
        self.ico_lock = tk.PhotoImage(data=img)
        self.cv.itemconfig(self.ilc, image=self.ico_lock)
        self.attributes('-topmost', self.ON_TOP)
        self.update()
        self.ON_TOP = not self.ON_TOP

    def izq(self, e):
        if self.OP>0.3:
            self.OP -= 0.1
            self.attributes('-alpha', self.OP)

    def der(self, e):
        if self.OP<1.0:
            self.OP += 0.1
            self.attributes('-alpha', self.OP)

    def normal(self, e):
        self.attributes('-alpha', 1)

    def muestra_tiempo(self):
        t, seg = self.obten_tiempo_hm()
        self.cv.itemconfig(self.TM, text=t)
        self.cv.itemconfig(self.SG, text=seg)
        self.cv.after(1000, self.muestra_tiempo)

    def obten_tiempo_hm(self):
        return time.strftime('%H:%M'), time.strftime('%S')
    

if __name__=="__main__":
    app = MiReloj()
    app.mainloop()