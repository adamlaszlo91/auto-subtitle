from abc import ABC, abstractmethod
import torch


class SpeechtoText(ABC):

    @abstractmethod
    def transcribe(self, waveform: torch.Tensor, sample_rate: int) -> str:
        pass
