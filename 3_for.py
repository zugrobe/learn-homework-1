"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
grade_sheet = [
    {'school_class': '1Г', 'scores': [5,4,4,5,3]},
    {'school_class': '3Ф', 'scores': [3,4,5,2,5,4]},
    {'school_class': '7В', 'scores': [4,4,4,5,5,3]},
    {'school_class': '8А', 'scores': [3,4,5,5,4,5,3]},
]

def school_average(school: list):
    result = 0
    for list_of_scores in school:
        result += (sum(list_of_scores['scores']) / len(list_of_scores['scores']))
    result = result / len(school)
    print('.')
    print('average count for school =', '%.2f' % result)
    print('.')

def class_average(school: list):
    result = 0
    for list_of_scores in school:
        result = sum(list_of_scores['scores']) / len(list_of_scores['scores'])
        print('average for group: ', list_of_scores['school_class'], ' =', '%.2f' % result)

def main(school: list):
    school_average(school)
    class_average(school)

if __name__ == "__main__":
    main(grade_sheet)
