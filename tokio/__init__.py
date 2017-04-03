from __future__ import absolute_import

try:
    import asyncio  # noqa
    from . import patch
    patch.patch_asyncio()
except ImportError:
    pass

from . import _ext

__all__ = ('new_event_loop', 'EventLoopPolicy')


def new_event_loop():
    return _ext.new_event_loop()


def spawn_event_loop(name='event-loop'):
    return _ext.spawn_event_loop(name)


class EventLoopPolicy:
    """Event loop policy."""

    def _loop_factory(self):
        return new_event_loop()
