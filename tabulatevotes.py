import csv
import pyrankvote
from pyrankvote import Candidate, Ballot
from rich import print

def load() -> tuple[list[str], list[dict[str, str]]]:
    """
    Loads data fom csv and choices.list.
    """
    # Read choices from choices.list
    with open('choices.list', 'r') as choices_file:
        choices = choices_file.read().splitlines()

    # Read ballots from ballots.csv
    with open('ballots.csv', 'r') as ballots_file:
        ballots = csv.DictReader(ballots_file)
        ballots = list(ballots)

    return choices, ballots

def tabulatevotes():
    """
    Tabulates the ballots.
    """
    rawchoices, rawballots = load()
    choices: dict[str, Candidate] = {choice: Candidate(choice) for choice in rawchoices}
    ballots = []
    for ballot in rawballots:
        ballots.append(Ballot(ranked_candidates=[choices[choice] for choice in ballot.values()]))
    result = pyrankvote.instant_runoff_voting(list(choices.values()), ballots)
    lastroundwinners = result.rounds[-1]
    print("Results:")
    winners = lastroundwinners.candidate_results
    wincount = 0
    for winner in winners:
        if winner.number_of_votes == 0:
            break
        wincount += 1
        print(f"[{'green' if wincount <= 2 else 'red'}]🎉 {winner.candidate.name}[/{'green' if wincount <= 2 else 'red'}]: {winner.number_of_votes}")


if __name__ == "__main__":
    tabulatevotes()