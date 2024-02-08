from commands import PlayerUpdateCmd

from ..base_screen import BaseScreen


class PlayerEdit(BaseScreen):
    """Screen displayed when editing a player (creating or changing an existing one)"""

    def __init__(self, club, player=None):
        self.club = club
        self.player = player

    def get_command(self):
        """Goes through the attributes and gets them from the user"""
        attrs = [
            ("name", "Player name", self.input_string),
            ("email", "Email address", self.input_email),
            ("chess_id", "Chess ID", self.input_chess_id),
            ("birthday", "Birthday", self.input_birthday),
        ]

        data = {}
        for key, prompt, func in attrs:
            kwargs = {"prompt": prompt}
            if self.player:
                kwargs.update(default=getattr(self.player, key))

            data[key] = func(**kwargs)

        return PlayerUpdateCmd(self.club, self.player, **data)
