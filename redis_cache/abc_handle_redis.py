from abc import ABC, abstractmethod


class AbcHandleRedis(ABC):

    @abstractmethod
    def load_cache(self)->None:
        raise NotImplementedError

    @abstractmethod
    def update_cache(self)->None:
        raise NotImplementedError