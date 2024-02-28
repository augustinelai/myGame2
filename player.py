from constant import Constant

class Player:
    def __init__(
        self, 
        name: str, 
        endowment: int, 
    ):
        self.name = name
        self.initial_endowment = endowment
        self.current_endowment = self.initial_endowment
        self.is_alive = True
        if self.initial_endowment >= Constant.RICH_LINE.value:
            self.assign_role('RICH')
        elif self.initial_endowment >= Constant.MIDDLE_LINE.value:
            self.assign_role('MIDDLE')
        else:
            self.assign_role('POOR')

    def health_check(self):
        if self.current_endowment <= 0:
            self.is_alive = False
        return self.is_alive

    def outflow(self, amount):
        print(f'{self.name} before outflow: {self.current_endowment}')
        self.current_endowment -= amount
        print(f'{self.name} after outflow: {self.current_endowment}')
        self.health_check()

    def inflow(self, amount):
        print(f'{self.name} before inflow: {self.current_endowment}')
        self.current_endowment += amount
        print(f'{self.name} after inflow: {self.current_endowment}')

    def assign_role(self, role_name):
        self.role = role_name

    def __str__(self) -> str:
        return f'I am {self.name}, a {self.role} now have {self.current_endowment}'
