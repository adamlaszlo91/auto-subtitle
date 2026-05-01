from speech_to_text.speech_to_text import SpeechtoText
import torch
import torchaudio  # type: ignore
import whisper  # type: ignore


class WhisperSpeechToTextImpl(SpeechtoText):

    def __init__(self) -> None:
        self._transcriber = whisper.load_model("tiny.en")

    def transcribe(self, waveform: torch.Tensor, sample_rate: int) -> str:
        waveform = waveform.mean(dim=0)
        if sample_rate != 16_000:
            waveform = torchaudio.transforms.Resample(sample_rate, 16000)(waveform)

        result = self._transcriber.transcribe(waveform)  # type: ignore
        return result["text"]  # type: ignore
