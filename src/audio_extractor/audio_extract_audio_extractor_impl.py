from audio_extractor.audio_extractor import AudioExtractor
from audio_extract import extract_audio  # type: ignore
from pathlib import Path


class AudioExtractAudioExtractorImpl(AudioExtractor):

    def extract(self, input_path: Path) -> Path:
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "audio.wav"

        if output_path.exists():
            output_path.unlink()

        print("Extracting audio...")
        extract_audio(input_path=input_path, output_path=str(output_path), output_format="wav")  # type: ignore
        print("Done.")
        return output_path
