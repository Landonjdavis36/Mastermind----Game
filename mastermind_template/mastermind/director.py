from game.board import board
from game.console import console
from game.move import move
from game.player import player
from game.roster import roster 

class director:


    def _init_(self):
    
        self._board = board()
        self._console = console()
        self._keep_playing = True
        self._move = None
        self._roster = roster()
    
    def start_game(self):

        self._prepare_game()
        while self._keep_playing:
            self._get_imputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game():



        for n in range(2):
            name = self._console.read(f"enter name of player {n + 1 }: ")
            player = player(name)
            self._roster.add_player(player)
    
    def _get_inputs(self):

        # display the game board
        board = self._board.to_string()
        self._console.write(board)
        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.read_number("what is your guess?")
        move = Move(guess)
        player.set_move(move)

    def _do_updates(self):

        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(player, move)

    def _do_outputs(self):

        if self._board.is_winner():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self._keep_playing = False
        self._roster.next_player()
        
















