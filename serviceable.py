from abc import ABC, abstractmethod

class Serviceable(ABC):
    def __init__(self) -> None :
        pass

    @abstractmethod
    def need_service(self) ->bool:
        pass