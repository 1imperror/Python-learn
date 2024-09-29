from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            increase = randint(50, 500)
            self.balance += increase
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {increase}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            reduce = randint(50, 500)
            print(f'Запрос на {reduce}')
            if reduce <= self.balance:
                self.balance -= reduce
                print(f'Снятие: {reduce}. Баланс: {self.balance}')
            elif reduce > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
