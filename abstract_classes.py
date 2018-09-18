from abc import ABC, abstractmethod


class abstract_animal(ABC):
    @abstractmethod
    def bark(self):
        print('bark')


class dog(abstract_animal):
    def bark(self):
        print('bow wow')


print(dog())
