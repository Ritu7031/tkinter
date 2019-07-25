import tkinter
from functools import partial
from handler import DataHandler

def open(name):
    for element in category_data labels:
        element.configure(text="")
        del elements

        list_data_for_category=data_handler.get_data_for_category(name)
        for i in range (len(list_data_for_category)):
            element=list.data_for_category)):
            label=tkinter.Label(window,text=element)
            label.grid(column=0,row=i+1)
            category_data_Labels,append(label)

window=tkinter.Tk()
window.title('book')
window.geometry('300x500')
data_handler=DataHandler("data1.json")
category_lists=data_handler.get_categories()
print(category_lists)
category_data_labels=[]

for i in range (len(category_lists)):
    element=category_lists[i]
    command=partial(open_category,element)
    button=tkinter.Button(window,text=element,command=command)
    button.grid(row=0,column=1)

window.mainloop()
                

