import logging
from pathlib import Path

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

try:
    import whisper
except ImportError as e:
    raise ImportError("Could not import Whisper. Run 'pip install git+https://github.com/openai/whisper.git'") from e

from speech2text.transcriber.base import BaseSpeechTranscriber


logger = logging.getLogger(__name__)


class WhisperTranscriber(BaseSpeechTranscriber):
    """
    Converts audio containing speech into its trascription using Whisper.
    """

    def __init__(
        self,
        model_size: Literal["tiny", "base", "small", "medium", "large"] = "base"
    ):
        super().__init__()
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_file: Path, sample_rate=16000) -> str:
        return self.model.transcribe(audio_file)["text"]

    def chunk(self, path: Path):
        yield path
