import tkinter
from functools import partial
from handler import DataHandler

def open_category(name):
    for element in category_data_labels:
        element.configure(text="")
        del element

    list_data_for_category=handler.get_data_for_category(name)
    print("list_data",list_data_for_category)
    for i in range (len(list_data_for_category)):
        element=list_data_for_category[i]
        label=tkinter.Label(window,text=element)
        label.grid(column=0,row=i+1)
        category_data_labels.append(label)

def Configure(event):
    canvas.configure(scrollregion=canvas.bbox(tkinter.ALL))

window=tkinter.Tk()
window.title('book')
canvas=tkinter.Canvas(window,bg='red')

window.geometry('100x100')
handler=DataHandler("data.json")
category_list=handler.get_categories()
print(category_list)
category_data_labels=[]

for i in range (len(category_list)):
    element=category_list[i]
    command=partial(open_category,element)
    button=tkinter.Button(window,text=element,command=command)
    button.grid(row=0,column=i)
    s=tkinter.Scrollbar(window,command=canvas.yview)
    canvas.configure(yscrollcommand=s.set)

window.mainloop()
                
