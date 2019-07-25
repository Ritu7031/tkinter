import json
class DataHandler:
    def __init__(self,file_name):
        file=open(file_name,'r')
        self.data1=json.load(file)

    def get_categories(self):
        list_data1=[]
        for element in self.data1["category_data"]:
            list_data1.append(element["name"])
        return list_data1

    def get_data_for_category(self,name):
        list_data1=[]
        for element in self.data1["category_data"]:
            if element["name"].lower()==name.lower():
                list_data1=element["list"]
        return list_data1

object1=DataHandler('data1.json')
print(object1.get_categories())
print(object1.get_data_for_category('employee'))
