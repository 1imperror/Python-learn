def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
#inner_function()
'''Выдаст ошибку. Имя не определено т.к. оно относится с локальной области видимости'''
