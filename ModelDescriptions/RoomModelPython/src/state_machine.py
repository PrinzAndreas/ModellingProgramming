# ------------------------------------------------------------
# This module defines a finite state machine (FSM) for room occupancy states
# The FSM manages transitions between states such as sleeping, working, airing, active, and preparing
# ------------------------------------------------------------

import random
import numpy as np
import pandas as pd

from transitions import Machine
from src.experiment import Experiment
from src.time_base_seconds import TimeUnits


def time_literal(t: str):
    parts = t.split(':')
    if len(parts) == 2:
        h, m = map(int, parts)
    if len(parts) == 3:
        h, m, s = map(int, parts)
        m += s / 60

    return h * 3600 + m * 60

class FSM(object):

    states = ['sleeping', 'working', 'airing', 'active', 'preparing']
    def __init__(self):
        self.tol     = 60                                   # Tolerance in seconds
        self.clock   = time_literal('00:00')                # Current time in seconds
        self.at_rand = {'airing': np.inf, 'active': np.inf} # Placeholders for random times

        self.transitions: list[dict] = [
            dict(source='preparing', dest='sleeping',  trigger='t_sleeping',  before=None,                  conditions=[]),
            dict(source='active',    dest='working',   trigger='t_working',   before=None,                  conditions=[lambda: self._time_condition(t=time_literal('10:00'))]),
            dict(source='airing',    dest='working',   trigger='t_working',   before=None,                  conditions=[lambda: self._time_condition(t=time_literal('10:00'))]),
            dict(source='active',    dest='preparing', trigger='t_preparing', before=None,                  conditions=[lambda: self._time_condition(t=time_literal('22:00'))]),
            dict(source='airing',    dest='preparing', trigger='t_preparing', before=None,                  conditions=[lambda: self._time_condition(t=time_literal('22:00'))]),
            dict(source='working',   dest='active',    trigger='t_active',    before=['set_random_times'],  conditions=[lambda: self._time_condition(t=time_literal('16:00'))]),
            dict(source='sleeping',  dest='active',    trigger='t_active',    before=['set_random_times'],  conditions=[lambda: self._time_condition(t=time_literal('06:00'))]),
            dict(source='airing',    dest='active',    trigger='t_active',    before=['set_random_times'],  conditions=[lambda: self._time_condition(t=self.at_rand['active'])]),
            dict(source='active',    dest='airing',    trigger='t_airing',    before=None,                  conditions=[lambda: self._time_condition(t=self.at_rand['airing'])]),
        ]

        self.machine = Machine(model=self, states=FSM.states, initial='sleeping', transitions=self.transitions)
        self.transitions = pd.DataFrame(self.transitions)
        self.last = None
        self.logs = []

    def _time_condition(self, t):
        now = self.clock
        return abs(t - now) < self.tol
    
    def __repr__(self):
        table = []
        for t in self.transitions:
            x = t.copy()
            x['conditions'] = any(_() for _ in x['conditions']) if x['conditions'] else None
            table.append(x)
        return pd.DataFrame(table).__repr__()

    def next_state(self, t: float):
        self.clock = t % (24 * TimeUnits.hour)
        mask = self.transitions['source'] == self.state
        for _, row in self.transitions[mask].iterrows():
            trigger = getattr(self, row['trigger'])
            trigger()
            if self.state == row['dest']:
                self.last = (row['source'], row['dest'])
                self.logs.append(
                    dict(
                        t=round(self.clock / TimeUnits.hour, 2),
                        source=row['source'],
                        dest=row['dest'],
                        action=self.last
                    )
                )
                return True

    def set_random_times(self):
        # Set random times for opening window
        delta = random.normalvariate(
            time_literal(Experiment.Variables.WINDOW_OPEN_NORMAL_MEAN),
            time_literal(Experiment.Variables.WINDOW_OPEN_NORMAL_STD),
        )
        open_at = (self.clock + delta) % (24 * TimeUnits.hour)
        self.at_rand['airing'] = open_at
    
        # Set random times for closing window
        delta = random.uniform(
            time_literal(Experiment.Variables.WINDOW_CLOSE_UNIFORM_LOW),
            time_literal(Experiment.Variables.WINDOW_CLOSE_UNIFORM_HIGH),
        )
        self.at_rand['active'] = (open_at + delta) % (24 * TimeUnits.hour)

