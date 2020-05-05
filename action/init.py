from .start import _start
from .help import _help
from .source import _source
from .echo import _echo
from .exit import _exit
from .prod import _prod


def init():
    _start()
    _help()
    _source()
    _prod()
    _echo()
    _exit()
    pass
