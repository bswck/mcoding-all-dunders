from __future__ import annotations

import builtins
import sys
from contextlib import suppress
from collections.abc import Mapping, Sequence


def import_called(
    name: str,
    globals: Mapping[str, object] | None = None,
    locals: Mapping[str, object] | None = None,
    fromlist: Sequence[str] = (),
    level: int = 0,
) -> None:
    print(name, fromlist, level)

__import__ = import_called

import plistlib  # doesn't work

# remove from cache
del plistlib
del sys.modules["plistlib"]

builtins.__import__ = import_called

import plistlib  # works
# plistlib None 0

with suppress(ImportError):
    from plistlib import FMT_BINARY
    # plistlib ('FMT_BINARY',) 0
