"""
Абстрактный класс
"""

from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def get_name(self):
        return 'human'
class worker(Human):
    def get_name(self):
        #return 'worker'
        return Human.get_name(self)

work = worker()

print(work.get_name())
