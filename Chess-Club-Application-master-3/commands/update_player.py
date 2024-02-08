from commands.context import Context

from .base import BaseCommand


class PlayerUpdateCmd(BaseCommand):
    """Command to update a player"""

    def __init__(self, club, player, **data):
        self.club = club
        self.player = player
        self.data = data

    def execute(self):
        """The command uses the update_player method from the Club model"""
        if self.player:
            player = self.club.update_player(self.player, **self.data)
        else:
            player = self.club.create_player(**self.data)

        return Context("player-view", club=self.club, player=player)
