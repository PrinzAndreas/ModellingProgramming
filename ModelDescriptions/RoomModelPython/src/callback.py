# ----------------------------------------------------------------
# This module contains callback functions for the ODE integrator
# Callbacks are functions that are called at specific events during the integration process
# They are used to update the state of the system, compute rates, and perform other necessary actions
# ----------------------------------------------------------------

import numpy as np
from src.odes import System
from src.experiment import Experiment
from src.tools import Event
from src.time_base_seconds import TimeUnits


def update_integrator(ode, **kwargs):
    kwargs['ics'][ode.notation] = ode.state
    kwargs['params'][f'{ode.notation}_rate'] = ode.rate

def update_rate(ode, **kwargs):
    ode.state = kwargs['c_step']['points'][ode.notation][-1]
    ode.dy_dt(t=kwargs['t'][-1])

def clb_env_temp(**kwargs):
    env = System.env
    env.state = env.compute_temp(t=kwargs['t'][-1])
    env.dy_dt(t=kwargs['t'][-1])
    # print('rate env', env.rate)
    #update_rate(ode=radiator, **kwargs)
    update_integrator(ode=env, **kwargs)

def clb_get_rates(**kwargs):
    room = System.room
    window_rate = System.window_rate
    opening_rate = System.opening_rate
    radiator = System.radiator
    
    window_rate.set_state(int(room.open))
    update_integrator(ode=window_rate, **kwargs)

    opening_rate.set_state(radiator.opening())
    update_integrator(ode=opening_rate, **kwargs)

def clb_log_callback(**kwargs):
    time_ = kwargs['c_step']['points']['t'][-1]
    print([time_/3600, time_, Experiment.integrator.tdata[-1]])

def clb_wanted_temp_callback(**kwargs):
    update_integrator(ode=System.wanted_temperature, **kwargs)

def clb_radiator_temp(**kwargs):
    update_rate(ode=System.radiator, **kwargs)
    update_integrator(ode=System.radiator, **kwargs)

def clb_room_temp(**kwargs):
    update_rate(ode=System.room, **kwargs)
    update_integrator(ode=System.room, **kwargs)

def clb_wake_up(**kwargs):
    TEMP_DAY_NOMINAL = Experiment.Variables.TEMP_DAY_NOMINAL
    System.wanted_temperature.set_state(state=TEMP_DAY_NOMINAL)
    System.radiator.tempNominal = TEMP_DAY_NOMINAL
    update_integrator(ode=System.radiator, **kwargs)

def clb_sleep(**kwargs):
    TEMP_NIGHT_NOMINAL = Experiment.Variables.TEMP_NIGHT_NOMINAL
    System.wanted_temperature.set_state(state=TEMP_NIGHT_NOMINAL)
    System.radiator.tempNominal = TEMP_NIGHT_NOMINAL
    update_integrator(ode=System.radiator, **kwargs)


def open_close_window_event(start, duration=None):
    duration = np.random.randint(1, 8)/10 if duration is None else duration
    duration += start
    open_window = Event(name='open_window_event', time=start, repeat=None)
    close_window = Event(name='close_window_event', time=duration, repeat=None)
    open_window.attach_callback(func=lambda **kwargs: System.room.set_open(open=True))
    close_window.attach_callback(func=lambda **kwargs: System.room.set_open(open=False))
    return open_window, close_window


def close_window(**kwargs):
    System.room.set_open(open=False)

def open_window(**kwargs):
    System.room.set_open(open=True)



CALLBACKS = {
    ('active', 'airing'): [open_window],
    ('active', 'working'): [close_window],
    ('active', 'preparing'): [close_window],
    ('airing', 'active'): [close_window],
    ('airing', 'preparing'): [close_window],
    ('airing', 'working'): [close_window],
    ('sleeping', 'active'): [clb_wake_up, clb_wanted_temp_callback],
    ('preparing', 'sleeping'): [clb_sleep, clb_wanted_temp_callback],
    None: [clb_env_temp, clb_get_rates, clb_wanted_temp_callback, clb_room_temp, clb_radiator_temp]
}



