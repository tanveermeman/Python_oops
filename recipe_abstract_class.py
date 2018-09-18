from abc import ABC, abstractmethod


class abstract_recipe(ABC):
    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


class recipe1(abstract_recipe):

    def prepare(self):
        print('do the dishes')
        print('get the raw material')

    def recipe(self):
        print('execute')

    def cleanup(self): pass


recipe1().execute()


