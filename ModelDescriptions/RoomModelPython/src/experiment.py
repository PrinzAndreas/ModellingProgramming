# ------------------------------------------------------------
# A set of global experiment variables
# ------------------------------------------------------------

from src.time_base_seconds import TimeUnits

class Experiment:
    integrator = None

    class Variables:
        TEMP_NIGHT_NOMINAL = 15
        TEMP_DAY_NOMINAL = 22
        EXPERIMENT_DURATION = 2*TimeUnits.day
        INTEGRATOR_PRECISION = 0.2
        WINDOW_OPEN_NORMAL_MEAN = '02:00'
        WINDOW_OPEN_NORMAL_STD = '00:30'
        WINDOW_CLOSE_UNIFORM_LOW = '00:05'
        WINDOW_CLOSE_UNIFORM_HIGH = '00:10'
        RADIATOR_TYPE = 'water'    
    
