from abc import ABC, abstractmethod
import time
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Espresso(Coffee):
    def prepare(self):
        print('preparing espresso...')

class Cappuccino(Coffee):
    def prepare(self):
        print('preparing cappuccino...')

class Latte(Coffee):
    def prepare(self):
        print('preparing latte...')

class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type =='Latte':
            return Latte()
        elif coffee_type =='Capuccino':
            return Cappuccino()
        else:
            raise ValueError('Unknown coffee type')
        
# c = Coffee() #can't instantiate an abstract class object
# latte = Latte()
# latte.prepare()

# print('----------')
# cap = Cappuccino()
# cap.prepare()

coffee_machine = CoffeeMachine()
try:
    coffee = coffee_machine.make_coffee('Latte')
    coffee.prepare()
    time.sleep(5) #just to add more realism to simulation
    print('Done.')
except ValueError as e:
    print(e)
