class MyError(Exception):
    def __init__(self, text='MyError'):
        self.text = text


def inputFromUser():
    b = int(input())
    if b == 0:
        raise MyError('Некорректное значение')
        # raise ValueError('Некорректное значение')
    return b


try:
    a = inputFromUser()
except Exception as e:
    print(e)
    a = 1
if a % 2 == 0:
    print(10 / a)
else:
    print(10 * a)
