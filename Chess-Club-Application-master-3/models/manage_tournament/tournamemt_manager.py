from tournament_util import (list_tournament_files, update_current_round, load_tournament_data, save_tournament_data,
                             modify_match, display_and_select_matches)
import os


def club_manager():
    tournaments_directory = "/Users/waltercueva/Downloads/Chess-Club-Application-master 3/data/tournaments"
    tournament_files = list_tournament_files(tournaments_directory)
    for index, file in enumerate(tournament_files, start=1):
        print(f"{index}. {file}")
    selected_index = int(input("Select a tournament by number: ")) - 1
    selected_file = tournament_files[selected_index]
    selected_file_path = os.path.join(tournaments_directory, selected_file)
    tournament = load_tournament_data(selected_file_path)
    while True:
        round_index, match_index = display_and_select_matches(tournament)
        if round_index is not None and match_index is not None:
            modify_match(tournament, round_index, match_index, selected_file_path)
        update_round = input("Do you want to update the current round? (yes/no): ").lower()
        if update_round == 'yes':
            update_current_round(tournament)
        save_tournament_data(selected_file_path, tournament)
        if tournament["completed"]:
            break
        if input("Do you want to continue modifying this tournament? (yes/no): ").lower() != "yes":
            break


if __name__ == "__main__":
    club_manager()
