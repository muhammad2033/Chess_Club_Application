from commands import ClubListCmd, NoopCmd

from ..base_screen import BaseScreen


class ClubView(BaseScreen):
    """Screen displayed when viewing a club"""

    def __init__(self, club):
        self.club = club

    def display(self):
        """Displays the club name and a list of players in the club (with numbers)"""
        print("##", self.club.name)
        for idx, p in enumerate(self.club.players, 1):
            print(idx, p.name, p.email)

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            print("Select a player to view/edit it, or 'C' to create a new player.")
            print("Type 'B' to go back to main menu.")
            value = self.input_string()
            if value.upper() == "B":
                return ClubListCmd()
            elif value.upper() == "C":
                return NoopCmd("player-create", club=self.club)
            elif value.isdigit():
                value = int(value)
                return NoopCmd(
                    "player-view", club=self.club, player=self.club.players[value - 1]
                )
