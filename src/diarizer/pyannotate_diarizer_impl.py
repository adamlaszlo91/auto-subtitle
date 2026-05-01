from diarizer.diarizer import Diarizer
from diarizer.diarizer_result import DiarizerResult
from pathlib import Path
from pyannote.audio import Pipeline
import torchaudio  # type: ignore


class PyannotateDiarizerImpl(Diarizer):

    def __init__(self) -> None:
        self._pipeline = Pipeline.from_pretrained(  # type: ignore
            Path("model") / "speaker-diarization-community-1"
        )

    def diarize(self, input_path: Path) -> list[DiarizerResult]:
        print("Beginning diarization...")
        results: list[DiarizerResult] = []
        waveform, sample_rate = torchaudio.load(input_path)  # type: ignore
        output = self._pipeline({"waveform": waveform, "sample_rate": sample_rate})  # type: ignore

        for turn, speaker in output.speaker_diarization:
            cut_waveform = waveform[
                :, int(turn.start * sample_rate) : int(turn.end * sample_rate)
            ]
            results.append(
                DiarizerResult(
                    speaker_id=speaker,
                    start_s=turn.start,
                    end_s=turn.end,
                    waveform=cut_waveform,
                )
            )

        print("Done.")
        return results
