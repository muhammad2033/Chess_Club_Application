from .base import BaseCommand
from .context import Context


class NoopCmd(BaseCommand):
    """Special command: does not do anything, just forwards the data to the screen specified"""

    def __init__(self, screen, **kwargs):
        """Constructor takes the screen name and its arguments"""
        self.screen = screen
        self.kwargs = kwargs

    def execute(self):
        """Forward the screen and arguments to the context"""
        return Context(self.screen, **self.kwargs)
