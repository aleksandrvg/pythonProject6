import random

# class MyError(Exception):
#     def __init__(self, text='MyError'):
#         self.text = text


# def inputFromUser():
#     b = int(input())
#     if b == 0:
#         # raise MyError('Некорректное значение')
#         raise ValueError('Некорректное значение')
#     return b
#
#
# try:
#     a = inputFromUser()
# except Exception as e:
#     print(e)
#     a = 1
# if a % 2 == 0:
#     print(10 / a)
# else:
#     print(10 * a)
#
#
# def someFunction():
#     er = False
#     try:
#         a = inputFromUser()
#         if a % 2 == 0:
#             print(10 / a)
#         else:
#             print(10 * a)
#     except:
#         er = True
#     finally:
#         return er


# def getText():
#     if random.randint(0, 1) == 1:
#         return 'text' * 2
#     else:
#         return 2
#
#
# file = open('test.txt', "w+", encoding="utf-8")
# try:
#     file.write(getText())
#     print(file.read())
# except TypeError:
#     file.write(str(getText()))
#     print(file.read())
# except:
#     print('Ошибка')
# finally:
#     file.close()


# try:
#     a = int(input())
#     out = a / random.randint(1, 10)
# except:
#     out = 'Ошибка ввода'
# finally:
#     print(out)


try:
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    out = a / b
except ValueError:
    out = 'Ошибка ввода'
except:
    out = 'Деление на ноль'
finally:
    print(out)
