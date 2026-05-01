from srt_generator.srt_generator import SrtGenerator
from diarizer.diarizer_result import DiarizerResult
from pathlib import Path


class PlainSrtGeneratorImpl(SrtGenerator):

    def generate(
        self,
        file_name: str,
        diarization_result: list[DiarizerResult],
        transcriptions: list[str],
    ):
        print("Writing srt...")

        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / file_name

        if output_path.exists():
            output_path.unlink()

        srt = "\n"
        for index, diarization in enumerate(diarization_result):
            start_hours, start_minutes, start_seconds, start_milliseconds = (
                self.convert_seconds(seconds=diarization.start_s)
            )
            end_hours, end_minutes, end_seconds, end_milliseconds = (
                self.convert_seconds(seconds=diarization.end_s)
            )
            start_timestamp_text = f"{start_hours:02d}:{start_minutes:02d}:{start_seconds:02d},{start_milliseconds:02d}"
            end_timestamp_text = f"{end_hours:02d}:{end_minutes:02d}:{end_seconds:02d},{end_milliseconds:02d}"

            srt = f"{srt}{index}\n{start_timestamp_text} --> {end_timestamp_text}\n[{diarization.speaker_id}] {transcriptions[index]}\n\n"

        with open(output_path, "w") as text_file:
            text_file.write(srt)

        print("Done.")

    def convert_seconds(self, seconds: float) -> tuple[int, int, int, int]:
        _hours = int(seconds // 3600)
        _minutes = int((seconds % 3600) // 60)
        _seconds = int(seconds % 60)
        _milliseconds = int((seconds - int(seconds)) * 1000)

        return _hours, _minutes, _seconds, _milliseconds
