from datetime import datetime


class Item: # Класс описывающий обьекты
    def __init__(self, *item):
        self.name = item[0]
        self.width = item[1]
        probel = item[-1].rfind(' ')
        self.cost = int(item[-1][probel:])
        
        
    def __str__(self):
            return "%s, %s,  %s" % (self.name, self.width,  self.cost)

class Storage: #Хранилка
    storage = {}
    change_time = {}
    
    def __init__(self):
        self.last_storage_id = 0
        
    def add_item(self, item): #Приход товара
        if len(self.storage) >= 10:
            print ('Storage is full')
        else:
            self.last_storage_id += 1
            self.storage[self.last_storage_id] = item
            self.change_time[self.last_storage_id] = ['Add_item - ' + str(datetime.now())]
        
    def return_item(self, key, item): # Возврат товара
        self.storage[key] = item
        self.change_time[self.last_storage_id] = ['Return_item - ' + str(datetime.now())]

        
    def search_item(self, key):
        print ("%s => %s" % (key, self.storage.get(key)))
        
    def delete_item(self, key):
        if key in self.storage:
            self.storage.pop(key)
            self.change_time[key].append('Del_item - ' + str(datetime.now()))
        else:
            return None
    
    def show_all(self):
        keys = self.storage.keys()
        for key in sorted(keys):
            print ("%s => %s" % (key, self.storage[key]))
    
    
class Store:
    storage = {} # для проданых
    refs ={} # для списанных
    log = {} 
    balans = 0
    balance_log = []
    
    def change_log(self, key, message): # Писалка в лог
        if key in self.log:
            self.log[key].append(message)
        else:
            self.log[key] = []
            self.log[key].append(message)
    
    
    def balans_update(self, name_storage, key, operand):
        price = name_storage.storage[key].cost
        if operand == '+':
            self.balans = self.balans + int(price)
            self.balance_log.append(str(datetime.now()) + ' Sell_item ' + str(key) + ' + ' + str(price) +', balans = ' + str(self.balans))
        else:
            self.balans = self.balans - int(price)
            self.balance_log.append(str(datetime.now()) + ' Return_item ' + str(key) + ' - ' + str(price) +', balans = ' + str(self.balans))
    
    def sell_item(self, name_storage, key):
        if key in name_storage.storage:
            self.balans_update(sklad, key, '+') #правим баланс
            self.storage[key] = name_storage.storage.get(key) # Добавляем себе в проданные
            name_storage.delete_item(key) # Удаляем со склада
            self.change_log(key, 'Sell_item - ' + str(datetime.now())) #логируемся
        else:
            print('Item not found')
                
            
    def return_to_store(self, name_storage, key): # Возврат товара
        if key in self.storage:
            self.balans_update(onliner, key, '-')
            name_storage.return_item(key, self.storage.get(key)) # добавляем товар обратно на склад
            self.storage.pop(key) # Удаляем из проданных
            self.change_log(key, 'Return_item - ' + str(datetime.now()))
        else:
            print('Item not found')
            
    def utilization_item(self, name_storage, key): # Списание товара
        if key in name_storage.storage:
            self.refs[key] = name_storage.storage.get(key)  # добавляем товар в списанные
            name_storage.delete_item(key) # Удаляем со склада
            self.change_log(key, 'Ref_item - ' + str(datetime.now())) # логируем
        else:
            print('Item not found')
        
            


sklad = Storage()
onliner = Store()



sklad.add_item(Item('Телевизор', 'марка: Samsung', '42', '2016 год выпуска', 'стоимость: 1500'))
sklad.add_item(Item('Телевизор', 'марка: LG', '56', '2017 год выпуска', 'стоимость: 725'))
sklad.add_item(Item('Мобильный телефон', 'марка: Samsung Galaxy J7', '5.5', '2017 год выпуска',
                    'оперативная память 3гб', 'флэш-память: 16г', 'камера', '13 Мп', 'стоимость: 6610'))
sklad.add_item(Item('Мобильный телефон', 'марка: Xiaomi Redmi 5', '5.7', '2017 год выпуска',
                    'оперативная память 3гб', 'флэш-память: 32г', 'камера 12 Мп', 'стоимость: 5200'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7',' 2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Стиральная машина', 'марка: BEKO WDI', 'наличие сушки: да', 'загрузка: 8кг',
                    'отжим: 1400 об/м', 'стоимость: 810'))
sklad.add_item(Item('Стиральная машина', 'марка: Electrolux EWG', 'наличие сушки: да', 'загрузка: 7кг',
                    'отжим: 1600 об/м', 'стоимость: 2300'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))
sklad.add_item(Item('Мобильный телефон', 'марка: iPhone 6s', '4.7', '2016 год выпуска',
                    'оперативная память 2гб', 'флэш-память: 64г', 'камера, 12 Мп', 'стоимость: 3750'))


onliner.sell_item(sklad, 1)
onliner.sell_item(sklad, 6)
onliner.sell_item(sklad, 3)
onliner.utilization_item(sklad, 4)
sklad.show_all()
print(onliner.balance_log)
onliner.return_to_store(sklad, 6)
print(onliner.balance_log)
onliner.utilization_item(sklad, 1)
onliner.sell_item(sklad, 5)
print(onliner.balans)


