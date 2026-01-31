## Python description of Room

[Python](https://www.python.org/) is a high-level programming language widely used for scientific computing and simulations.
It is used in this implementation to describe the room model and run experiments with it.

The [Python model description](https://github.com/PrinzAndreas/ModellingProgramming/tree/main/ModelDescriptions/RoomModelPython) includes the following files.

* [main.ipynb](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/main.ipynb) - main program and experiment description
* [heating_constants.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/heating_constants.py) - constants used for the heating model
* [experiment.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/experiment.py) - experiment configuration and variables
* [odes.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/odes.py) - ordinary differential equations for the model

Moreover, the following Python modules are used.

* [time_base_seconds.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/time_base_seconds.py) - establishing seconds as time granularity
* [integrator.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/integrator.py) - handling of differential equations
* [tools.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/tools.py) - integration tools using PyDSTool
* [value_table.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/value_table.py) - using tables of time-value pairs
* [state_machine.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/state_machine.py) - describing discrete behaviour as state machines
* [callback.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/callback.py) - callback functions for the ODE integrator

The Python descriptions can be executed using Python 3.6 with the required packages installed (see [requirements.txt](cs/requirements.txt)).

