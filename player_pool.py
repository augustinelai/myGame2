from player import Player
from typing import Dict

class PlayerPool:
    def __init__(self):
        self.participants_pool: Dict[str, Player] = dict()
        self.collective_contribution = 0
        self.commited_resources = 0

    def reset_pool(self):
        self.participants_pool = dict()

    def reset_contribution(self):
        self.collective_contribution = 0

    def add_resource(self, amount):
        print(f'Before adding resource, amount is {self.collective_contribution}')
        self.collective_contribution += amount
        print(f'Before adding resource, amount is {self.collective_contribution}')

    def commit_payout_resource(self, amount):
        print(f'Commit payout amount {amount} on {self.collective_contribution}')
        self.commited_resources += amount
        return amount

    def spend_resource(self):
        print(f'Before spending resource, amount is {self.collective_contribution}')
        self.collective_contribution -= self.commited_resources
        print(f'After spending resource, amount is {self.collective_contribution}')
        self.commited_resources = 0

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