"""
This script allows anyone to create a JSON file for a chess club.
It will be filled with random members.
"""
import argparse
import json
import random

# Using Faker to generate data
from faker import Faker
from faker.providers import BaseProvider


class ChessID(BaseProvider):
    """Custom provider class to generate a 'Chess ID'"""

    def chess_id(self):
        """Chess ID = two letters + 5 numbers"""
        # Letters
        elements = [chr(random.randint(65, 90)) for _ in range(2)]
        # Numbers
        elements.extend([str(random.randint(0, 9)) for _ in range(5)])
        return "".join(elements)


ATTRS = ("name", "email", "chess_id")


def make_club(name, fname=None, count=20):
    """Main function to generate a club"""
    # Set up Faker and add the custom provider
    fake = Faker()
    fake.add_provider(ChessID)

    # Start with the club name
    data = {"name": name}
    # Add the players from Faker
    data["players"] = [
        {key: getattr(fake, key)() for key in ATTRS} for _ in range(count)
    ]

    # Generate birthdays, but make sure that the player is not too young
    for player in data["players"]:
        birthdate = fake.date_of_birth()
        while birthdate.year > 2008:
            birthdate = fake.date_of_birth()
        # And store the dates as string for JSON serialization
        player["birthday"] = birthdate.strftime("%d-%m-%Y")

    if not fname:
        # We did not get a file name: generate it
        fname = name.replace(" ", "") + ".json"

    with open("clubs/" + fname, "w") as fp:
        json.dump(data, fp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a JSON file for a club.")
    # Club name (required)
    parser.add_argument("clubname", type=str, help="club name")
    # File name (not required)
    parser.add_argument("filename", type=str, nargs="?", help="JSON file name")
    # Number of players (not required)
    parser.add_argument(
        "--count", type=int, nargs="?", help="Number of players to generate"
    )

    args = parser.parse_args()
    make_club(name=args.clubname, fname=args.filename, count=args.count)
