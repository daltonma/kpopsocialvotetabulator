import config
import csv
import pyrankvote
from pyrankvote import Candidate, Ballot
from rich import print

def load() -> tuple[list[str], list[dict[str, str]]]:
    """
    Loads data fom csv and choices.list.
    """
    # Read choices from choices.list
    with open(config.CHOICES_FILE, 'r') as choices_file:
        choices = choices_file.read().splitlines()

    # Read ballots from ballots.csv
    with open(config.BALLOTS_FILE, 'r') as ballots_file:
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
    result = pyrankvote.single_transferable_vote(list(choices.values()), ballots, number_of_seats=config.SEATS)
    lastroundwinners = result.rounds[-1]
    print("Results:")
    winners = lastroundwinners.candidate_results
    for winner in winners[0:config.SEATS]:
        print(f"[bold green]🎉 {winner.candidate.name}[/bold green] - {winner.number_of_votes:.2f} votes")


if __name__ == "__main__":
    tabulatevotes()