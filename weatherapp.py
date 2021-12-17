
import tkinter as tk
#from tkinter import font
from requests_html import HTMLSession


root = tk.Tk()

def retornoDatos(arg=None):
    sesion = HTMLSession()
    query = ciudad.get()
    try:
        url = f'https://www.google.com/search?q=clima+{query}'
        response = sesion.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

        temperatura = response.html.find('span#wob_tm', first=True).text
        unidades = response.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        descripcion = response.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
        ubicacion_label.config(text=query.capitalize())
        temperatura_label.config(text=temperatura)
        celcius_label.config(text=unidades)
        descripcion_label.config(text=descripcion)
    except:
        ubicacion_label.config(text='ERROR. Localidad no encontrada')
    finally:
            ciudad.delete(0, tk.END)

ciudad = tk.Entry(root, width=20)
ciudad.focus()
ciudad.bind('<Return>', retornoDatos)
ciudad.place(x=20, y=10)

ubicacion_label = tk.Label(root,text="",font=("Times", "20","italic"),bg='#8573DF')
ubicacion_label.place(x=10, y=50)

temperatura_label = tk.Label(root,text="",font=("Times", "40","italic"),bg='#8573DF')
temperatura_label.place(x=10, y=95)

celcius_label = tk.Label(root,text="",font=("Times", "14","italic"),bg='#8573DF')
celcius_label.place(x=68, y=95)

descripcion_label = tk.Label(root,text="",font=("Times", "14","italic"),bg='#8573DF')
descripcion_label.place(x=10, y=160)


root.geometry('200x200')
root['bg'] = '#8573DF'
root.resizable(0,0)

root.mainloop()
