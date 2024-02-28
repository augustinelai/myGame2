from player import Player
from typing import Dict

class PlayerPool:
    def __init__(self):
        self.participants_pool: Dict[str, Player] = dict()
        self.collective_contribution = 0

    def reset_pool(self):
        self.participants_pool = dict()

    def reset_contribution(self):
        self.collective_contribution = 0

    def add_resource(self, amount):
        self.collective_contribution += amount

    def get_resource(self, proportion):
        outflow = round(self.collective_contribution * proportion, -1)
        self.collective_contribution -= outflow
        return outflow

    def add_player(self, *players: Player):
        for player in players:
            if player.name not in self.participants_pool:
                self.participants_pool[player.name] = player
                return True
            else:
                print(f'Player {player.name} already in Player Pool')
                return False

    def remove_player(self, *players: Player):
        for player in players:
            if player.name in self.participants_pool:
                self.participants_pool.pop(player.name, None)
                return True
            else:
                print(f'Player {player.name} not in Player Pool')
                return False