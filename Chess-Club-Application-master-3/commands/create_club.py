from commands.context import Context
from models import ClubManager

from .base import BaseCommand


class ClubCreateCmd(BaseCommand):
    """Command to create a club"""

    def __init__(self, name):
        self.name = name

    def execute(self):
        """Uses a ClubManager instance to create the club and add it to the list of managed clubs"""
        cm = ClubManager()
        club = cm.create(self.name)
        return Context("club-view", club=club)
