"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    def compare_strings(one, two):
        if type(one) is not str or type(two) is not str:
            return '0'
        elif (one) == (two):
            return '1'
        elif (one) != (two) and (two) == 'learn':
            return '3' 
        elif (one) != (two) and len(one) > len(two):
            return '2'
        else:
            return 'Первое слово короче, а второе не "learn".'  

    e = compare_strings('yellow', 1)
    print(e)
    e = compare_strings('yellow', 'duck')
    print(e)
    e = compare_strings('duck', 'learnPY123')
    print(e)
    e = compare_strings('yellow', 'learn')
    print(e)
    
if __name__ == "__main__":
    main()
