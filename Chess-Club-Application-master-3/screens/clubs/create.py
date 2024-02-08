from commands import ClubCreateCmd

from ..base_screen import BaseScreen


class ClubCreate(BaseScreen):
    """Screen displayed when creating a club"""

    display = "## Create club"

    def get_command(self):
        print("Type in the name of the club")
        name = self.input_string()

        return ClubCreateCmd(name)
