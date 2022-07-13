import abc
from abc import abstractmethod


class Galeria(metaclass=abc.ABCMeta):
    @abstractmethod
    def agregar(self):
        raise NotImplementedError