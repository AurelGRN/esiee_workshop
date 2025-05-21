"""
class dog:
    def __init__(self, color, eye_color, height, lenght, weight):
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.lenght = lenght
        self.weight = weight

    def sit(self):
        print("the dog sits")
    
    def lay_down(self):
        print("the dog lay downs")

    def shake(self):
        print("the dog shake")

    def come(self):
        print("the dog come next to you")

class cat:
    def __init__(self, color, eye_color, height, lenght, weight):
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.lenght = lenght
        self.weight = weight

Mohammed = dog("malicious","brown", 10,12,15)
Didi = cat("puple","brown", 25,22,30)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          # public
        self._balance = balance     # protected
        self.__pin = "1234"         # private

    def deposit(self, amount):      # public
        self._balance += amount

    def withdraw(self, amount):     # public
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def check_funds(self):         # public
        print(f"Balance: {self._balance}")

    def __check_pin(self):         # private
        print("Verifying PIN...")

account = BankAccount("John", 100)
account.deposit(50)
account.withdraw(20)
account.check_funds()

# Accès aux membres
print(account.owner)      # OK (public)
print(account._balance)   # OK mais pas recommandé (protected)

"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Mammal(Animal):
    def __init__(self, species, has_fur):
        super().__init__(species)
        self.has_fur = has_fur

    def move(self):
        print("The mammal moves on land.")


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(species="Platypus", has_fur=True)
        self.name = name
        self.has_bill = True
        self.can_swim = True
        self.lays_eggs = True

    def eat(self):
        print(f"{self.name} eats insects and small aquatic animals.")

    def swim(self):
        print(f"{self.name} is swimming.")


p = Platypus("Teddy")
p.move()
p.eat()
p.swim()
print(f"Fur: {p.has_fur}, Bill: {p.has_bill}, Lays eggs: {p.lays_eggs}")
