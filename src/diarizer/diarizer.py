from diarizer.diarizer_result import DiarizerResult
from abc import ABC, abstractmethod
from pathlib import Path


class Diarizer(ABC):

    @abstractmethod
    def diarize(self, input_path: Path) -> list[DiarizerResult]:
        pass
