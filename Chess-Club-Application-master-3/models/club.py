import json

from .player import Player


class ChessClub:
    """
    A local chess club.

    Data is loaded from a JSON file (provided as argument).
    The class creates Player instances based on JSON data.
    """

    def __init__(self, filepath=None, name=None):
        """The constructor works in two ways:
        - if the filepath is provided, it loads data from JSON
        - if it is not but a name is provided, it creates a new club (and a new JSON file)
        """

        self.name = name
        self.filepath = filepath
        self.players = []

        if filepath and not name:
            # Load data from the JSON file
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                self.players = [
                    Player(**player_dict) for player_dict in data["players"]
                ]
        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Serializes the players and saves the club info to the JSON file"""

        with open(self.filepath, "w") as fp:
            json.dump(
                {"name": self.name, "players": [p.serialize() for p in self.players]},
                fp,
            )

    def create_player(self, **kwargs):
        """Utility method to create a new player instance and add it to the club"""

        player = Player(**kwargs)
        self.players.append(player)
        self.save()
        return player

    def update_player(self, player, **kwargs):
        """Utility method to update a player instance based on arguments provided"""

        if player not in self.players:
            raise RuntimeError(f"Player {player} not in club {self.name}!")

        for key, value in kwargs.items():
            setattr(player, key, value)

        self.save()
        return player
