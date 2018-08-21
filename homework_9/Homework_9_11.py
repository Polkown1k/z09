from datetime import datetime


class Item: # Класс описывающий обьекты
    def __init__(self, name, width, year, cost):
        self.name = name
        self.width = width
        self.year = year
        self.cost = cost
        
    def __str__(self):
            return "%s, %s, %s, %s" % (self.name, self.width, self.year, self.cost)

class Storage: #Хранилка
    storage = {}
    change_time = {}
    
    def __init__(self):
        self.last_storage_id = 0
        
    def add_item(self, item):
        self.last_storage_id += 1
        self.storage[self.last_storage_id] = item
        self.change_time[self.last_storage_id] = 'Add_item - ' + str(datetime.now())
        
    def search_item(self, key):
        print ("%s => %s" % (key, self.storage.get(key)))
        
    def delete_item(self, key):
        if key in self.storage:
            self.storage.pop(key)
            self.change_time[key] = self.change_time[key] + ', Del_item - ' + str(datetime.now())
        else:
            return None
    
    def show_all(self):
        keys = self.storage.keys()
        for key in sorted(keys):
            print ("%s => %s" % (key, self.storage[key]))
    
    
        
        


storage = Storage()
a = Item('TV', 'Samsung', 2018, 600)
b = Item('Phone', 'Sony', 2013, 100)
storage.add_item(a)
storage.add_item(b)

#print(storage.change_time)
storage.show_all()
storage.search_item(1)
print('ddddddddddddddddddddddddddd')
storage.delete_item(1)
storage.show_all()
print(storage.change_time)

