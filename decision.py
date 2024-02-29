def naive_hardworking(number_of_turns):
    rich_decision = [
        # (produce, get_reward_proportion)
        (0, 0.25) for i in range(number_of_turns)
    ]

    middle_decision = [
        # (produce, get_reward_proportion)
        (2, 0.2) for i in range(number_of_turns)
    ]

    poor_decision = [
        # (produce, get_reward_proportion)
        (2, 0.2) for i in range(number_of_turns)
    ]
    return rich_decision, middle_decision, poor_decision

def naive_layback(number_of_turns):
    rich_decision = [
        # (produce, get_reward_proportion)
        (0, 0.25) for i in range(number_of_turns)
    ]

    middle_decision = [
        # (produce, get_reward_proportion)
        (1, 0.2) for i in range(number_of_turns)
    ]

    poor_decision = [
        # (produce, get_reward_proportion)
        (1, 0.2) for i in range(number_of_turns)
    ]
    return rich_decision, middle_decision, poor_decision

def naive_strike(number_of_turns):
    rich_decision = [
        # (produce, get_reward_proportion)
        (0, 0.25) for i in range(number_of_turns)
    ]

    middle_decision = [
        # (produce, get_reward_proportion)
        (0, 0.2) for i in range(number_of_turns)
    ]

    poor_decision = [
        # (produce, get_reward_proportion)
        (0, 0.2) for i in range(number_of_turns)
    ]
    return rich_decision, middle_decision, poor_decision