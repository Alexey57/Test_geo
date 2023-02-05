from tkinter import *
import tkintermapview
from rosreestr2coord import Area


def clicked():
    res = txt.get()
    area = Area(res)
    list = area.get_coord()
    list = list[0][0]

    list_path = []
    for i in range(len(list)):
        point = ()
        list[i][0], list[i][1] = list[i][1], list[i][0]
        point = (list[i][0], list[i][1])
        list_path.append(point)

    map_widget.set_position(52.26667269308686, 104.63460124177388)  # Paris, France
    map_widget.set_zoom(16)

    polygon_1 = map_widget.set_polygon(list_path)

    print(list_path[0])


window = Tk()
window.title("Test_geo")
window.geometry('800x600+0+0')

lbl = Label(window, text="Введите кадастровый номер")
lbl.grid(column=0, row=0)

txt = Entry(window, width=30)
txt.grid(column=1, row=0)

map_widget = tkintermapview.TkinterMapView(window, width=1600, height=900, corner_radius=0)
map_widget.place(relx=0, rely=0.05)

btn = Button(window, text="Ввод", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()


# ("38:06:144003:4723")