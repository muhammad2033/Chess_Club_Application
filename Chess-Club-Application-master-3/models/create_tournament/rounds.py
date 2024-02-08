def distribute_into_rounds(pairings):
    round_data = []
    while pairings:
        round_matches = []
        players_in_round = set()

        for pairing in pairings[:]:
            if pairing[0] not in players_in_round and pairing[1] not in players_in_round:
                round_matches.append({"players": list(pairing), "completed": False, "winner": None})
                players_in_round.update(pairing)
                pairings.remove(pairing)

        if round_matches:
            round_data.append(round_matches)

    return round_data
