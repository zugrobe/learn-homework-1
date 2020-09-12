"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    
    dict = {"key": "value", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Дуб дерево?": "Нет.", "Динамо бежит?": "Все бегут"}

    while True:
        user_say = input('Спрашивай: ')

        try:
            if user_say in dict.keys():
                print('value')
                #print(dict[])
                break
            else:
                print('Я не на экзамене: {}'.format(user_say))
        except ValueError:
            print("Пока")
            break
    
if __name__ == "__main__":
    ask_user()
