import json
import os
from models.player import list_club_files, get_player_ids_from_club
from matches import generate_pairings
from rounds import distribute_into_rounds


def create_chess_tournament():
    clubs_directory = '/Users/waltercueva/Downloads/Chess-Club-Application-master 3/data/clubs'
    club_files = list_club_files(clubs_directory)
    for index, file in enumerate(club_files, start=1):
        print(f"{index}. {file}")

    while True:
        try:
            selected_index = int(input("Select a club by number: ")) - 1
            # Validate if selected index is within the range of available clubs
            if selected_index < 0 or selected_index >= len(club_files):
                print("Invalid number. Please select a valid club number.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    selected_club_file = club_files[selected_index]
    player_ids = get_player_ids_from_club(os.path.join(clubs_directory, selected_club_file))

    tournament_data = {
        "name": input("Enter tournament name: "),
        "dates": {"from": input("Enter start date (DD-MM-YYYY): "), "to": input("Enter end date (DD-MM-YYYY): ")},
        "venue": input("Enter venue: "),
        "number_of_rounds": int(input("Enter number of rounds: ")),
        "current_round": 1,
        "completed": False,
        "players": player_ids,
        "rounds": []
    }

    pairings = generate_pairings(tournament_data["players"])
    tournament_data["rounds"] = distribute_into_rounds(pairings)

    filename = (f"{tournament_data['name'].replace(' ', '_').lower()}"
                f"-{'completed' if tournament_data['completed'] else 'in-progress'}.json")
    save_directory = '/Users/waltercueva/Downloads/Chess-Club-Application-master 3/data/tournaments'
    os.makedirs(save_directory, exist_ok=True)
    file_path = os.path.join(save_directory, filename)

    with open(file_path, 'w') as json_file:
        json.dump(tournament_data, json_file, indent=4)
    print(f"JSON file created: {file_path}")


if __name__ == "__main__":
    create_chess_tournament()
