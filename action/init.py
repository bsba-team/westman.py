from .start import _start
from .help import _help
from .source import _source
from .echo import _echo


def init():
    _start()
    _help()
    _source()
    _echo()
    pass
