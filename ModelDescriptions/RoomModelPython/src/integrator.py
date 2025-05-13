from src.odes import *
from src.experiment import *
from src.callback import *
from src.tools import  *

def init_integrator():
        
    main_event = Event(name='main_event', time=0 * TimeUnits.second, repeat=Experiment.Variables.INTEGRATOR_PRECISION * TimeUnits.minute, term=True, active=True)
    wake_up_event = Event(name='wake_up_event', time=7 * TimeUnits.hour, repeat=24*TimeUnits.hour)
    go_to_sleep_event = Event(name='go_to_sleep_event', time=22 * TimeUnits.hour, repeat=24*TimeUnits.hour)

    main_event.attach_callback(func=clb_env_temp)
    main_event.attach_callback(func=clb_get_rates)
    main_event.attach_callback(func=clb_wanted_temp_callback)
    main_event.attach_callback(func=clb_room_temp)
    main_event.attach_callback(func=clb_radiator_temp)

    wake_up_event.attach_callback(func=clb_wake_up)

    go_to_sleep_event.attach_callback(func=clb_sleep)


    Experiment.integrator = Integrator(
        tdata=[0, Experiment.Variables.EXPERIMENT_DURATION],
        max_step=10 * TimeUnits.minute,
        min_step=0.0001 * TimeUnits.minute,
        init_step=10*TimeUnits.second,
        expressions={
            **System.room.expr, 
            **System.radiator.expr, 
            **System.env.expr, 
            **System.boiler.expr, 
            **System.window_rate.expr, 
            **System.wanted_temperature.expr, 
            **System.opening_rate.expr
        },
        ics={
            **System.room.ics, 
            **System.radiator.ics, 
            **System.env.ics, 
            **System.boiler.ics, 
            **System.window_rate.ics, 
            **System.wanted_temperature.ics, 
            **System.opening_rate.ics
        },
        events=[
            main_event,
            wake_up_event,
            go_to_sleep_event,
            *open_close_window_event(start=7.35*TimeUnits.hour, duration=0.35*TimeUnits.hour),
            *open_close_window_event(start=15.7*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=17*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=18.2*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=20.9*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=22*TimeUnits.hour, duration=0.25*TimeUnits.hour),
            *open_close_window_event(start=(24 + 17)*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=(24 + 18.2)*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=(24 + 20.9)*TimeUnits.hour, duration=0.3*TimeUnits.hour),
            *open_close_window_event(start=(24 + 22)*TimeUnits.hour, duration=0.25*TimeUnits.hour),
        ],
        params={
            'env_rate': System.env.dy_dt(t=0),
            'room_rate': System.room.dy_dt(t=0),
            'radiator_rate': System.radiator.dy_dt(t=0),
            'boiler_rate': System.boiler.dy_dt(t=0),
            'window_rate': System.window_rate.dy_dt(t=0),
            'wanted_rate': System.wanted_temperature.dy_dt(t=0),
            'opening_rate': System.opening_rate.dy_dt(t=0),
        }
    )
    
    System.env.refresh_value_table()
    Experiment.integrator.verbose = 1
    