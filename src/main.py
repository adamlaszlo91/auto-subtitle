from audio_extractor.audio_extractor import AudioExtractor
from audio_extractor.audio_extract_audio_extractor_impl import (
    AudioExtractAudioExtractorImpl,
)
from pathlib import Path


def main():
    # TODO: Use argument
    input_path = Path("input") / "Alfred_Hitchcock_Extended_Interview.ogv.240p.vp9.webm"
    audio_extractor: AudioExtractor = AudioExtractAudioExtractorImpl()
    audio_extractor.extract(input_path=input_path)


if __name__ == "__main__":
    main()
