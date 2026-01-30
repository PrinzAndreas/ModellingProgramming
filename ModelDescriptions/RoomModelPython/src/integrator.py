# ------------------------------------------------------------
# This module initializes and configures the ODE integrator
# ------------------------------------------------------------


from src.odes import *
from src.experiment import *
from src.callback import *
from src.tools import  *
from src.state_machine import FSM

fsm = FSM()

def fsm_callback(**kwargs):
    # Request next state
    current_time = kwargs['c_step']['points']['t'][-1]
    fsm.next_state(current_time)
    
    # Get last transition
    transition = fsm.last
    
    # Call default callbacks
    for f in CALLBACKS[None]:
        f(**kwargs)

    # Call transition specific callbacks
    if transition is not None and transition in CALLBACKS:
        for f in CALLBACKS[transition]:
            f(**kwargs)


def init_integrator():

    # An event stops the integrator at specified intervals to perform some actions
    main_event = Event(
        name='main_event',                  
        time=0 * TimeUnits.second,                                              # Starts immediately
        repeat=Experiment.Variables.INTEGRATOR_PRECISION * TimeUnits.minute,    # Repeats at specified intervals
        term=True,                                                              # Terminates the integrator when triggered
        active=True                                                             # Is active                          
    )
    
    # Attach the FSM callback to the main event
    # This callback will be called every time the event is triggered
    # Updates the FSM state and performs associated actions
    main_event.attach_callback(func=fsm_callback)


    # Set up the integrator
    Experiment.integrator = Integrator(

        # Duration and step sizes
        tdata=[0, Experiment.Variables.EXPERIMENT_DURATION],
        max_step=10 * TimeUnits.minute,
        min_step=0.0001 * TimeUnits.minute,
        init_step=10*TimeUnits.second,

        # Events
        events=[main_event],

        # Expressions (ODEs), initial conditions and parameters
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
    
    # Reset environements and logs
    System.env.refresh_value_table()
    Experiment.integrator.verbose = 1
    fsm.logs = []
    