class Roster:

    def __init__(self):

        self.current = 0
        self.players = []

    def add_player(self, player):

        if player not in self.players:
            self.players.append(player)

    def get_current(self):

        return self.players[self.current]

    def next_player(self):

        self.current = (self.current + 1) % len(self.players)
        

