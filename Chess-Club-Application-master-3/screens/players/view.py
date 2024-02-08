from commands import NoopCmd

from ..base_screen import BaseScreen


class PlayerView(BaseScreen):
    """Screen displayed when viewing a Player"""

    def __init__(self, club, player=None):
        self.club = club
        self.player = player

    def display(self):
        print("##", self.club.name)
        print("###", self.player.name)
        print("Email:", self.player.email)
        print("Chess ID:", self.player.chess_id)
        print("Birthdate:", self.player.birthday)

    def get_command(self):
        while True:
            print("Type 'E' to edit the player, or 'B' to go back to club view.")
            action = self.input_string()
            if action.upper() == "B":
                return NoopCmd("club-view", club=self.club)
            elif action.upper() == "E":
                return NoopCmd("player-edit", club=self.club, player=self.player)
