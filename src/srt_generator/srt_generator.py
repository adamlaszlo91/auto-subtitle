from abc import ABC, abstractmethod
from diarizer.diarizer_result import DiarizerResult


class SrtGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        file_name: str,
        diarization_result: list[DiarizerResult],
        transcriptions: list[str],
    ):
        pass
