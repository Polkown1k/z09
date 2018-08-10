# z09
# Задача #3: Написать функцию, будет считать буквы переданной ей строки. 
# a = 'hello' *порядок букв не обязателен. Пример calculate_chars(a) >> 'h - 1, e - 1, l - 2, o - 1'


def calculate_chars(some_string):
    set_string = set(some_string)
    dic_result = {}
    for i in set_string:
        counter = some_string.count(i)
        temp_dic = {i: counter}
        dic_result.update(temp_dic)
    print(dic_result)

calculate_chars("batya mojet")


# Задача #2: Написать функцию, которая будет корректно сравнивать "версии". 
# a = '1.15' b = '1.15.4' Пример compare_version(a, b) >> '1.15' < '1.15.4'

def compare_version(first, second):
    
    def a_win():
        print(first,'>',second)
        return
    
    def b_win():
        print(first,'<',second)
        return
    
    list_first = first.split('.')
    list_second = second.split('.')
    lenhgt_first = len(list_first)
    lenght_second = len (list_second)
    min_lenght = min(lenhgt_first,lenght_second)
    
    
    
    for i in range(min_lenght):
        temp_first = int(list_first[i])
        temp_second = int(list_second[i])
        if temp_first > temp_second:
            a_win()
            return
        
        elif temp_first < temp_second:
            b_win()
            return
        
    if lenhgt_first > lenght_second:
        a_win()
        return
    elif lenhgt_first < lenght_second:
        b_win()
        return
        
    print(first,'=',second)
    return
        

compare_version('2.172', '2.17.444444')