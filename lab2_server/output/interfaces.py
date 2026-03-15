from abc import ABC, abstractmethod
from typing import Dict


class OutputStrategy(ABC):
    @abstractmethod
    def send(self, record: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
