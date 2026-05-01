from audio_extractor.audio_extractor import AudioExtractor
from audio_extractor.audio_extract_audio_extractor_impl import (
    AudioExtractAudioExtractorImpl,
)
from diarizer.diarizer import Diarizer
from diarizer.pyannotate_diarizer_impl import PyannotateDiarizerImpl
from speech_to_text.speech_to_text import SpeechtoText
from speech_to_text.whisper_speech_to_text_impl import WhisperSpeechToTextImpl
from srt_generator.srt_generator import SrtGenerator
from srt_generator.plain_srt_generator_impl import PlainSrtGeneratorImpl
from pathlib import Path


def main():
    # TODO: Use argument
    input_path = Path("input") / "The_YouTube_Interview_with_President_Obama_part.webm"

    audio_extractor: AudioExtractor = AudioExtractAudioExtractorImpl()
    diarizer: Diarizer = PyannotateDiarizerImpl()
    speech_to_text: SpeechtoText = WhisperSpeechToTextImpl()
    srt_generator: SrtGenerator = PlainSrtGeneratorImpl()

    audio_path = audio_extractor.extract(input_path=input_path)
    diarization_result = diarizer.diarize(input_path=audio_path)
    transcriptions: list[str] = []
    for result in diarization_result:
        print(f"{result.speaker_id}\t{result.start_s:.3f} : {result.end_s:.3f}")
        transciption = speech_to_text.transcribe(
            waveform=result.waveform, sample_rate=result.sample_rate
        )
        print(transciption)
        transcriptions.append(transciption)
    # TODO: Depend on input file name
    srt_generator.generate(
        file_name="The_YouTube_Interview_with_President_Obama_part.srt",
        diarization_result=diarization_result,
        transcriptions=transcriptions,
    )


if __name__ == "__main__":
    main()
