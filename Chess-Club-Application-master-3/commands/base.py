from abc import ABCMeta, abstractmethod


class BaseCommand(metaclass=ABCMeta):
    """This is the base class for a command"""

    @abstractmethod
    def execute(self):
        """Abstract method: child classes must implement it!"""
        pass

    def __call__(self):
        """Syntactic sugar: calling the instance calls its execute() method"""
        return self.execute()
