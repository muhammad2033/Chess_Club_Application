## Points system

Each player will gain points depending on their match results.
* When a player wins a match, they get 1 point
* When a player loses a match, they get 0 point
* When there is no result (draw match), each player gets 0.5 point

## Chess tournament matchmaking rules

### Round 1

Shuffle the list of players, and pair them randomly.

Example:
| Player   | Player   | Result        | Player points | Player points |
| -------- | -------- | ------------- | ------------- | ------------- |
| Player 1 | Player 2 | Player 1 wins | 1             | 0             |
| Player 3 | Player 4 | Player 3 wins | 1             | 0             |
| Player 5 | Player 6 | draw          | 0.5           | 0.5           |
| Player 7 | Player 8 | draw          | 0.5           | 0.5           |

The players can now be ranked:
| Player   | Points |
| -------- | ------ |
| Player 1 | 1      |
| Player 3 | 1      |
| Player 5 | 0.5    |
| Player 6 | 0.5    |
| Player 7 | 0.5    |
| Player 8 | 0.5    |
| Player 2 | 0      |
| Player 4 | 0      |

### Following rounds

Sort the players by their tournament points (descending), and pair players in order (#1 with #2, #3 with #4, etc).
* If two players have the same number of points, randomly pick one.
* The match making system should **try** to prevent identical matches (same players playing against each other several times).

### Round 2

With round 1 played before (see above), the next round may be:

| Player   | Player   | Result        | Player points | Player points |
| -------- | -------- | ------------- | ------------- | ------------- |
| Player 1 | Player 3 | Player 3 wins | 1             | 2             |
| Player 5 | Player 7 | Player 5 wins | 1.5           | 0.5           |
| Player 6 | Player 8 | draw          | 1             | 1             |
| Player 2 | Player 4 | Player 4 wins | 0             | 1             |

* Player 5 plays against player 7, but they could have played against Player 8: the opponent was randomly chosen.
* Player 5 would not play against Player 6, because they already played against each other in round 1.

Rankings are now:
| Player   | Points |
| -------- | ------ |
| Player 3 | 2      |
| Player 5 | 1.5    |
| Player 1 | 1      |
| Player 6 | 1      |
| Player 8 | 1      |
| Player 4 | 1      |
| Player 7 | 0.5    |
| Player 2 | 0      |

### Round 3

Given the round 2 above, the next round may be:
* Player 3 vs Player 5
* Player 1 vs Player 6
* Player 8 vs Player 4
* Player 7 vs Player 2

### Repeat the processes as many times as required