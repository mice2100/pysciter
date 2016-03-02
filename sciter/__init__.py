"""Sciter bindings for Python."""

from .scapi import SciterAPI
from .value import value as Value
from .window import Window
from .dom import Element
from .event import EventHandler
from .error import SciterError, ScriptError, ScriptException, ValueError
from .sctypes import SCITER_WIN, SCITER_OSX, SCITER_LNX

sapi = api = SciterAPI()
gapi = sapi.GetSciterGraphicsAPI if sapi else None
rapi = sapi.GetSciterRequestAPI if sapi else None


def version(as_str=False):
    """Return version of Sciter engine as (3,3,1,7) tuple or '3.3.1.7' string."""
    high = api.SciterVersion(True)
    low = api.SciterVersion(False)
    ver = (high >> 16, high & 0xFFFF, low >> 16, low & 0xFFFF)
    return ".".join(map(str, ver)) if as_str else ver


def script(name=None):
    """Annotation decorator for the functions that called from script."""
    # @script def -> script(def)
    # @script('name') def -> script(name)(def)
    def decorator(func):
        attr = True if name is None else name
        func._from_sciter = attr
        return func
    if isinstance(name, str):
        return decorator
    func = name
    name = None
    return decorator(func)
