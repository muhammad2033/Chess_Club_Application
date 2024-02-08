from commands.context import Context

from .base import BaseCommand


class ExitCmd(BaseCommand):
    """Special command: it stops the application from running"""

    def execute(self):
        return Context(run=False)
