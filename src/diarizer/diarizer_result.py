from dataclasses import dataclass
import torch


@dataclass
class DiarizerResult:
    speaker_id: str
    start_s: float
    end_s: float
    sample_rate: int
    waveform: torch.Tensor
