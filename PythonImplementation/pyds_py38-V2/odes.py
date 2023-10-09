import numpy as np


class ODE:
    def __init__(self, notation):
        self.notation = notation
        self.expr = {self.notation: f'{self.notation}_rate'}
        self.rate = 0
        self.state = 0

        self.dq = 0


    def update_state(self, state_value):
        self.state = state_value

    def dy_dt(self, t):
        pass

    @property
    def ics(self):
        return {self.notation: self.state}


class Environment(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)
        self.state = 7.5

    @classmethod
    def compute_temp(cls, t):
        return 5 * np.sin(2 * np.pi * (t/3600 - 10)/24) + 10

    def dy_dt(self, t):
        self.rate = self.state - self.compute_temp(t=t)
        return self.rate


class Boiler(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)
        self.state = 40

    def dy_dt(self, t):
        return 0