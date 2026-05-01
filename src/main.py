from audio_extractor.audio_extractor import AudioExtractor
from audio_extractor.audio_extract_audio_extractor_impl import (
    AudioExtractAudioExtractorImpl,
)
from diarizer.diarizer import Diarizer
from diarizer.pyannotate_diarizer_impl import PyannotateDiarizerImpl
from pathlib import Path


def main():
    # TODO: Use argument
    input_path = Path("input") / "The_YouTube_Interview_with_President_Obama_part.webm"

    audio_extractor: AudioExtractor = AudioExtractAudioExtractorImpl()
    diarizer: Diarizer = PyannotateDiarizerImpl()

    audio_path = audio_extractor.extract(input_path=input_path)
    diarization_result = diarizer.diarize(input_path=audio_path)
    for result in diarization_result:
        print(f"{result.speaker_id}\t{result.start_s:.3f} : {result.end_s:.3f}")


if __name__ == "__main__":
    main()
