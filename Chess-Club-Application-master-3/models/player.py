from datetime import datetime
import json
import os


class Player:
    """The player class holds all information related to a player"""

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, name, email, chess_id, birthday):
        if not name:
            raise ValueError("Player name is required!")

        self.name = name
        self.email = email
        self.chess_id = chess_id

        # The class uses a private attribute for the birthdate (datetime format)
        self._birthdate = None
        # And a public one with a getter/setter for the birthday (str)
        self.birthday = birthday

    def __str__(self):
        return f"<{self.name}>"

    def __hash__(self):
        """Returns the hash of the object - useful to use the instance as a key in a dictionary or in a set"""
        return hash((self.name, self.email, self.chess_id, self.birthdate))

    def __eq__(self, other):
        """Required when __hash__ is defined"""
        if type(other) is not type(self):
            raise TypeError("'=' is not supported with type %s" % type(other))

        return (self.name, self.email, self.chess_id, self.birthdate) == (
            other.name,
            other.email,
            other.chess_id,
            other.birthdate,
        )

    @property
    def birthday(self):
        """Property to get the birthday (string) from the birthdate (datetime)"""
        return self.birthdate.strftime(self.DATE_FORMAT)

    @birthday.setter
    def birthday(self, value):
        """Sets the birthdate (datetime) from a string"""
        self.birthdate = datetime.strptime(value, self.DATE_FORMAT)

    def serialize(self):
        """Serialize the instance in a format compatible with JSON"""

        data = {attr: getattr(self, attr) for attr in ("name", "email", "chess_id")}
        # We make sure to use the str representation of the date
        # datetime is notnatively serializable in JSON
        data["birthday"] = self.birthday
        return data


def list_club_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.json')]


def get_player_ids_from_club(file_path):
    with open(file_path, 'r') as file:
        club_data = json.load(file)
        return [player['chess_id'] for player in club_data['players']]
