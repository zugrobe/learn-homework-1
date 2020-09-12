"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():

  def get_doing(usr_age):
      if 0 <= usr_age <= 6:
          return 'Goto: watch «Telepuziki»'
      elif 7 <= usr_age <= 15:
          return 'Goto: school'
      elif 16 <= usr_age <= 24:
          return 'Goto: university'
      elif 25 <= usr_age <= 60:
          return 'Goto: job'
      elif 61 <= usr_age <= 98:
          return '/*babka-mode on*/'
      else:
          return 'Кто здесь?'

  name = input('Сколько тебе лет (введи число): ')

  e = get_doing(int(name))
  print(e)

if __name__ == "__main__":
    main()
