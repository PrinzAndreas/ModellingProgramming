# ------------------------------------------------------------------
# This module defines the ODE classes for the room heating model
# ------------------------------------------------------------------

import numpy as np
from src.heating_constants import *
from src.experiment import Experiment
from src.value_table import ValueTable, autofill_and_initiate_value_table, VALUE_TABLE_PATH, INDEX_COL


# Base ODE class
# expression are essentially:
#  notation = rate
# rate is computed in dy_dt
# and states are updated using callbacks
# see callback.py

class ODE:
    def __init__(self, notation):
        self.notation = notation
        self.expr = {self.notation: f'{self.notation}_rate'}
        self.rate = 0
        self.state = 0

        self.dq = 0
        
    def dy_dt(self, t):
        pass

    @property
    def ics(self):
        return {self.notation: self.state}


class Boiler(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)
        self.state = 40

    def dy_dt(self, t):
        return 0


class Rate(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)

    def dy_dt(self, t):
        self.rate = 0
        return 0

    def set_state(self, state):
        self.state = state


class Environment(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)
        self.vTable = self.get_value_table()
        self.state = self.vTable.currentTemp

    def compute_temp(self, t):
        # return 5 * np.sin(2 * np.pi * (t/3600 - 10)/24) + 10
        return self.vTable.linear(t)

    def dy_dt(self, t):
        vt = self.compute_temp(t=t)
        self.rate = self.state - vt
        self.rate = (self.vTable.nextTemp - vt) / (self.vTable.nextTime - self.vTable.currentTime)
        return self.rate

    @staticmethod
    def get_value_table():
        return autofill_and_initiate_value_table(csv_path=VALUE_TABLE_PATH, value_table=ValueTable(unit=TimeUnits.hour), index_col=INDEX_COL)

    def refresh_value_table(self):
        self.vTable = self.get_value_table()


class Room(ODE):
    def __init__(self, notation):
        super().__init__(notation=notation)
        self.state = Experiment.Variables.TEMP_NIGHT_NOMINAL
        self.open = False

    def dy_dt(self, t):
        radiator_power = K_RADIATOR * A_RADIATOR * (System.radiator.state - self.state)
        wall_loss_rate = A_WALL * K_WALL * (self.state - System.env.state)
        window_loss_rate = A_WINDOW * {False: U.wi_closed, True: U.wi_open}[self.open] * (self.state - System.env.state)
        self.rate = (radiator_power - window_loss_rate - wall_loss_rate) / (C_AIR * D_AIR * V_ROOM)
        return self.rate

    def set_open(self, open):
        self.open = open


class Radiator(ODE):
    def __init__(self, notation, hyst=1):
        super().__init__(notation=notation)
        self.on: bool = False
        self.state = Experiment.Variables.TEMP_NIGHT_NOMINAL
        self.tempNominal = Experiment.Variables.TEMP_NIGHT_NOMINAL
        self.hyst = hyst
        self.temp_diff = 0

    def dy_dt(self, t):
        opening = self.opening()
        self.dq = (self.state - System.room.state) * A_RADIATOR * U.he
        dt_gain = opening * (F_WATER / V_RADIATOR) * (System.boiler.state - self.state)
        dt_loss = self.dq / (D_AIR * C_WATER * V_RADIATOR)
        self.rate = dt_gain - dt_loss
        return self.rate

    def opening(self):
        self.temp_diff = self.tempNominal - System.room.state
        if self.temp_diff <= 0:
            res = 0

        elif self.temp_diff >= self.hyst:
            res = 1

        else:
            res = self.temp_diff / self.hyst

        return res


class WaterRadiator(Radiator):
    def __init__(self, notation, init_temp, init_hyst):
        super().__init__(notation=notation, hyst=init_hyst)
        self.hyst = init_hyst
        self.state = init_temp

    def dy_dt(self, t):
        temp_in = System.boiler.state
        opening = self.opening()
        T1 = opening * (F_WATER / V_RADIATOR_WATER) * (temp_in - self.state)
        T2 = K_RADIATOR * A_RADIATOR * (System.room.state - self.state) / (V_RADIATOR_WATER * D_WATER * C_WATER)
        self.rate = T1 + T2
        return self.rate


class ElectricalRadiator(Radiator):
    def __init__(self, notation, init_hyst, init_temp):
        super().__init__(notation=notation, hyst=init_hyst)
        self.state = init_temp
        self.hyst = init_hyst

    def dy_dt(self, t):
        inpPower = (self.opening() * P_RADIATOR) / (C_WATER * V_RADIATOR_WATER * D_WATER)
        outPower = K_RADIATOR * A_RADIATOR * (System.room.state - self.state) / (V_RADIATOR_WATER * D_WATER * C_WATER)
        self.rate = inpPower + outPower
        return self.rate

# Single variable to hold all ODE instances
class System:
    env: Environment = None
    boiler: Boiler = None
    room: Room = None
    water_radiator: WaterRadiator = None
    electric_radiator: ElectricalRadiator = None
    radiator: Radiator = None
    window_rate: Rate = None
    opening_rate: Rate = None
    wanted_temperature: Rate = None



# Instantiate the ODE's
def init_odes():
    radiator_type = {
        'water': 0,
        'electric': 1
    }.get(Experiment.Variables.RADIATOR_TYPE, 0)

    System.env = Environment(notation='env')
    System.boiler = Boiler(notation='boiler')
    System.room = Room(notation='room')
    System.water_radiator = WaterRadiator(notation='radiator', init_temp=Experiment.Variables.TEMP_NIGHT_NOMINAL, init_hyst=1)
    System.electric_radiator = ElectricalRadiator(notation='radiator', init_temp=Experiment.Variables.TEMP_NIGHT_NOMINAL, init_hyst=0.2)
    System.radiator = [System.water_radiator, System.electric_radiator][radiator_type]
    System.window_rate = Rate(notation='window')
    System.opening_rate = Rate(notation='opening')
    System.wanted_temperature = Rate(notation='wanted')
    System.wanted_temperature.state = Experiment.Variables.TEMP_NIGHT_NOMINAL  # Set the initial states
    System.room.state = Experiment.Variables.TEMP_NIGHT_NOMINAL  # Set the initial states
