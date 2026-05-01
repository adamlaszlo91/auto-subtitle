from abc import ABC, abstractmethod
from pathlib import Path


class AudioExtractor(ABC):

    @abstractmethod
    def extract(self, input_path: Path) -> Path:
        pass
