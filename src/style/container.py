from abc import ABC, abstractmethod


class Container(ABC):
    @abstractmethod
    def get_container(self):
        raise NotImplemented
