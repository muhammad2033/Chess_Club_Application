from commands.context import Context
from models import ClubManager

from .base import BaseCommand


class ClubListCmd(BaseCommand):
    """Command to get the list of clubs"""

    def execute(self):
        cm = ClubManager()
        return Context("main-menu", clubs=cm.clubs)
