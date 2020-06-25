import time
from random import randint
import logging
import sys

def log(decorator):
    def new_decorator(*args, **kwargs):
        start = time.time()
        message = decorator(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        if exec_time < 0.1:
            exec_time = "{0:5.3f} ms".format((exec_time*1000))
        else:
            exec_time = "{0:5.3f} s ".format(exec_time)
        logging.basicConfig(filename='machine.log', format='%(message)s')
        logging.warning("(fablin)Running: {0:20}[ exec-time {1} ]".format(decorator.__name__.replace("_", " "), exec_time))
        return message
    return new_decorator

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)