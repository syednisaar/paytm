class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls_faced = 0

    def update_runs(self, runs):
        self.runs += runs
        self.balls_faced += 1

    def __str__(self):
        return f"{self.name} - Runs: {self.runs}, Balls Faced: {self.balls_faced}"


class CricketMatch:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.team1_score = 0
        self.team2_score = 0
        self.wickets_team1 = 0
        self.wickets_team2 = 0
        self.overs = 0
        self.current_team = team1
        self.current_batsman = 0

    def update_score(self, runs):
        player = self.current_team[self.current_batsman]
        player.update_runs(runs)
        self.team1_score += runs if self.current_team == self.team1 else self.team2_score
        self.overs += 0.1  # Simulating the passage of time in overs

        # Check if the batsman is out
        if runs == 0:  # Assuming '0' means the player is out
            self.current_batsman += 1
            if self.current_team == self.team1:
                self.wickets_team1 += 1
            else:
                self.wickets_team2 += 1

        # Switch teams after all wickets are down
        if self.wickets_team1 == len(self.team1) or self.wickets_team2 == len(self.team2):
            self.switch_teams()

    def switch_teams(self):
        if self.current_team == self.team1:
            self.current_team = self.team2
        else:
            self.current_team = self.team1
        self.current_batsman = 0

    def display_scores(self):
        print(f"\nScores after {int(self.overs)} overs:")
        print(f"Team 1: {self.team1_score} (Wickets: {self.wickets_team1})")
        print(f"Team 2: {self.team2_score} (Wickets: {self.wickets_team2})")
        print(f"Current batsman: {self.current_team[self.current_batsman].name}")
        print("Player Details:")
        for player in self.current_team:
            print(player)

def main():
    # Define teams and players
    team1 = [Player("Player 1A"), Player("Player 2A"), Player("Player 3A")]
    team2 = [Player("Player 1B"), Player("Player 2B"), Player("Player 3B")]

    match = CricketMatch(team1, team2)

    # Simulate the match (you can extend this to accept user input or random events)
    match.update_score(4)  # Player hits 4 runs
    match.update_score(1)  # Player hits 1 run
    match.update_score(0)  # Player gets out
    match.update_score(6)  # Player hits a six

    # Display current match status
    match.display_scores()

if __name__ == "__main__":
    main()
