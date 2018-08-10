# z09
Задача #3: Написать функцию, будет считать буквы переданной ей строки. 
a = 'hello' *порядок букв не обязателен. Пример calculate_chars(a) >> 'h - 1, e - 1, l - 2, o - 1'


def calculate_chars(some_string):
    set_string = set(some_string)
    dic_result = {}
    for i in set_string:
        counter = some_string.count(i)
        temp_dic = {i: counter}
        dic_result.update(temp_dic)
    print(dic_result)

calculate_chars("batya mojet")

