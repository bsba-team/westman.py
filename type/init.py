from .message import _message
from .photo import _photo
from .video import _video
from .music import _music
from .document import _document


def init():
    _message()
    _photo()
    _video()
    _music()
    _document()
    pass
