import random

class Board

    def __init__(self):
        
        self._state = {}
        # self._state stores the state of the board in the form:
        # {"player1 name": (current_guess, current_hint, number_to_guess),
        #  "player2 name": (curren_guess, current_hint, number_to_guess)
        # }

    def to_string(self):
        output = "\n---------------------\n"
        for name, value in self._state.items():
            output += f"player {name}: {value[0]}, {value[1]}\n"
        output += "---------------------\n"
        return output

    def is_winner(self):

        for value in self._state.values():
            if value[0] == value[2]:
                return True
        return False

    def apply(self, player, move):

        name = player.get_name()
        guess = str(move.get_guess())

        # Add player to board state if they don't already exist
        if not name in self._state:

            # store the player's state. the third position is the number
            # to guess
            self._state[name] = ("----", "****", str(random.randint(1111,9999)))

        # Get the number to guess the tuple
        _,_,number = self._state[name]

        # Get a hint based on the player's current state and guess
        hint = self._get_hint(name, guess)
        self._state[name] = (guess, hint, number)

    def _get_hint(self, player, move):

        number_to_guess = self._state[player][2]
        hint = ['*'] * 4
        for pos, digit in enumerate(move):
            if digit == number_to_guess[pos]:
                hint[pos] = 'x'
            elif digit in number_to_guess:
                hint[pos] = 'o'
            else:
                hint[pos] = '*'
        return "".join(hint)
