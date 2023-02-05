from tkinter import *
import tkintermapview
from rosreestr2coord import Area


def clicked():
    res = txt.get()
    area = Area(res)
    list = area.get_coord()
    if list and list[0]:
        list = list[0][0]

    list_path = []
    for item in list:
        point = ()
        item[0], item[1] = item[1], item[0]
        point = (item[0], item[1])
        list_path.append(point)

    map_widget.set_position(list_path[0][0],list_path[0][1])
    map_widget.set_zoom(16)

    polygon_1 = map_widget.set_polygon(list_path)


window = Tk()
window.title("Test_geo")
window.geometry('800x600+0+0')

lbl = Label(window, text="Введите кадастровый номер")
lbl.grid(column=0, row=0)

txt = Entry(window, width=30)
txt.grid(column=1, row=0)

map_widget = tkintermapview.TkinterMapView(window, width=800, height=600, corner_radius=0)
map_widget.place(relx=0, rely=0.05)

btn = Button(window, text="Ввод", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()


# ("38:06:144003:4723")
