from src.time_base_seconds import TimeUnits

class Experiment:
    integrator = None

    class Variables:
        TEMP_NIGHT_NOMINAL = 15
        TEMP_DAY_NOMINAL = 22
        EXPERIMENT_DURATION = 2*TimeUnits.day
        INTEGRATOR_PRECISION = 0.2
        
    
