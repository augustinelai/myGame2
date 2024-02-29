from abc import ABC, abstractmethod
from constant import Constant
from player import Player
from player_pool import PlayerPool

class Role(ABC):
    @abstractmethod
    def produce(self):
        pass
    
    @abstractmethod
    def consume(self):
        pass

    @abstractmethod
    def get_reward(self):
        pass

class RichRole(Role):
    def __init__(self, player: Player, player_pool: PlayerPool):
        self.player = player
        self.player_pool = player_pool

    def produce(self, contribute_level: int):
        if not self.player.health_check():
            return
        self.player_pool.add_player(self.player)
        # self.player_pool.add_resource(0)
        print(self.player)

    def consume(self):
        if not self.player.health_check():
            return
        self.player.outflow(Constant.RICH_SPEND.value)
        print(self.player)

    def get_reward(self, proportion):
        if not self.player.health_check():
            return
        reward_threshold = Constant.RICH_REMAINING_PROPORTION.value / \
            len([p for p in self.player_pool.participants_pool.values() if p.role == 'RICH'])
        if (0 <= proportion) and (proportion <= reward_threshold) and \
            (self.player.name in self.player_pool.participants_pool):
            amount = round(self.player_pool.collective_contribution * proportion, -1)
            self.player.inflow(self.player_pool.commit_payout_resource(amount))
        print(self.player)

class MiddleRole(Role):
    def __init__(self, player: Player, player_pool: PlayerPool):
        self.player = player
        self.player_pool = player_pool
        self.spend_level = Constant.MIDDLE_SPEND_IDLE.value

    def produce(self, contribute_level: int):
        if not self.player.health_check():
            return
        if contribute_level == 1:
            self.player_pool.add_player(self.player)
            self.player_pool.add_resource(Constant.MIDDLE_CONTRIBUTE_LESS.value)
            self.spend_level = Constant.MIDDLE_SPEND_LESS.value
        elif contribute_level == 2:
            self.player_pool.add_player(self.player)
            self.player_pool.add_resource(Constant.MIDDLE_CONTRIBUTE_MORE.value)
            self.spend_level = Constant.MIDDLE_SPEND_MORE.value
        else:
            self.spend_level = Constant.MIDDLE_SPEND_IDLE.value
        print(self.player)

    def consume(self):
        if not self.player.health_check():
            return
        self.player.outflow(self.spend_level)
        print(self.player)

    def get_reward(self, proportion):
        if not self.player.health_check():
            return
        reward_threshold = round(Constant.MIDDLE_REMAINING_PROPORTION.value / \
            len([p for p in self.player_pool.participants_pool.values() if p.role == 'MIDDLE']), 1)
        if (0 <= proportion) and (proportion <= reward_threshold) and \
            (self.player.name in self.player_pool.participants_pool):
            amount = round(self.player_pool.collective_contribution * proportion, -1)
            self.player.inflow(self.player_pool.commit_payout_resource(amount))
        print(self.player)

class PoorRole(Role):
    def __init__(self, player: Player, player_pool: PlayerPool):
        self.player = player
        self.player_pool = player_pool
        self.spend_level = Constant.POOR_SPEND_IDLE.value

    def produce(self, contribute_level: int):
        if not self.player.health_check():
            return
        if contribute_level == 1:
            self.player_pool.add_player(self.player)
            self.player_pool.add_resource(Constant.POOR_CONTRIBUTE_LESS.value)
            self.spend_level = Constant.POOR_SPEND_LESS.value
        elif contribute_level == 2:
            self.player_pool.add_player(self.player)
            self.player_pool.add_resource(Constant.POOR_CONTRIBUTE_MORE.value)
            self.spend_level = Constant.POOR_SPEND_MORE.value
        else:
            self.spend_level = Constant.POOR_SPEND_IDLE.value
        print(self.player)

    def consume(self):
        if not self.player.health_check():
            return
        self.player.outflow(self.spend_level)
        print(self.player)

    def get_reward(self, proportion):
        if not self.player.health_check():
            return
        reward_threshold = round(Constant.POOR_REMAINING_PROPORTION.value / \
            len([p for p in self.player_pool.participants_pool.values() if p.role == 'POOR']), 1)
        if (0 <= proportion) and (proportion <= reward_threshold) and \
            (self.player.name in self.player_pool.participants_pool):
            amount = round(self.player_pool.collective_contribution * proportion, -1)
            self.player.inflow(self.player_pool.commit_payout_resource(amount))
        print(self.player)
