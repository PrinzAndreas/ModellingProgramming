## Python Description of Room

[Python](https://www.python.org/) is a general-purpose programming language.
Using some libraries, it can be used to describe simulations.
The book sketches how the room model can be described using Python such that one can run experiments with it.

* Work in progress
![work in progress](../../images/comingSoon.png "work in progress")

The [Python model description](https://github.com/PrinzAndreas/ModellingProgramming/tree/main/ModelDescriptions/RoomModelPython) includes the following files.

* [main.ipynb](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/main.ipynb) - main program and experiment description
* [heating_constants.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/heating_constants.py) - constants used for the heating model
* [odes.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/odes.py) - differential equations for all entities
* [time_base_seconds.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/time_base_seconds.py) - establishing seconds as time granularity
* [tools.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/tools.py) - integrator for the differential equations and time handling
* [value_table.py](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/src/value_table.py) - using tables of values

### How to run 
1. Install [Gnuplot](https://sourceforge.net/projects/gnuplot/)
2. Install [PyCharm](https://www.jetbrains.com/pycharm/) or any other Python tool with Python 3.8.
3. Install the [requirements.txt](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/requirements.txt) file in PyCharm or by running the command `pip install -r requirements.txt` within a terminal from the project directory.
4. Open the [main.ipynb](https://github.com/PrinzAndreas/ModellingProgramming/blob/main/ModelDescriptions/RoomModelPython/main.ipynb) notebook and run all cells.
