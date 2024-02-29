from role import Role, RichRole, MiddleRole, PoorRole
from constant import Constant
from player import Player
from player_pool import PlayerPool
from decision import naive_hardworking, naive_layback, naive_strike

PLYAER_POOL = PlayerPool()

RICH_LIST: Role = [
    RichRole(Player('R1', Constant.RICH_LINE.value), PLYAER_POOL),
    RichRole(Player('R2', Constant.RICH_LINE.value), PLYAER_POOL)
]
MIDDLE_LIST: Role = [
    MiddleRole(Player('M1', Constant.MIDDLE_LINE.value), PLYAER_POOL),
    MiddleRole(Player('M2', Constant.MIDDLE_LINE.value), PLYAER_POOL),
    MiddleRole(Player('M3', Constant.MIDDLE_LINE.value), PLYAER_POOL)
]
POOR_LIST: Role = [
    PoorRole(Player('P1', Constant.POOR_LINE.value), PLYAER_POOL),
    PoorRole(Player('P2', Constant.POOR_LINE.value), PLYAER_POOL),
    PoorRole(Player('P3', Constant.POOR_LINE.value), PLYAER_POOL),
    PoorRole(Player('P4', Constant.POOR_LINE.value), PLYAER_POOL),
    PoorRole(Player('P5', Constant.POOR_LINE.value), PLYAER_POOL)
]

NUMBER_OF_ROUNDS = 10
rich_decision, middle_decision, poor_decision = naive_layback(NUMBER_OF_ROUNDS)

for i in range(NUMBER_OF_ROUNDS):
    print(f'Round {i+1}')
    # Produce Stage
    for role in RICH_LIST:
        role.produce(rich_decision[i][0])
    for role in MIDDLE_LIST:
        role.produce(middle_decision[i][0])
    for role in POOR_LIST:
        role.produce(poor_decision[i][0])

    # Reward Stage
    for role in RICH_LIST:
        role.get_reward(rich_decision[i][1])
    PLYAER_POOL.spend_resource()
    for role in MIDDLE_LIST:
        role.get_reward(middle_decision[i][1])
    PLYAER_POOL.spend_resource()
    for role in POOR_LIST:
        role.get_reward(poor_decision[i][1])
    PLYAER_POOL.spend_resource()

    # Reset every round
    PLYAER_POOL.reset_contribution()

    # Consume Stage
    for role in RICH_LIST + MIDDLE_LIST + POOR_LIST:
        role.consume()
            