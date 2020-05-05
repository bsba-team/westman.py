from .message import _message
from .photo import _photo
from .video import _video
from .audio import _audio
from .document import _document
from .sticker import _sticker


def init():
    _message()
    _photo()
    _video()
    _audio()
    _document()
    _sticker()
    pass
